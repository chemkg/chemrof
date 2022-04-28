/*

  Examples of use:

  See Makefile.etl
  
  pq-ontobee -e --consult src/prolog/chebi.pro "conjugate(A,B,AN,BN,ACh,BCh)"

  */

:- use_module(library(sparqlprog/dataframe)).
:- use_module(library(sparqlprog/owl_util)).

:- use_module(library(semweb/rdf_library)).
:- use_module(library(semweb/rdf_http_plugin)).
:- use_module(library(semweb/rdf_cache)).
:- use_module(library(semweb/turtle)).
:- use_module(library(semweb/rdf_zlib_plugin)).
:- use_module(library(semweb/rdf11)).
:- use_module(library(semweb/rdfs)).
:- use_module(library(semweb/rdf_turtle)).
:- use_module(library(semweb/rdf_ntriples)).

:- rdf_register_prefix('CHEBI','http://purl.obolibrary.org/obo/CHEBI_').
:- rdf_register_prefix('chem','https://w3id.org/chemschema/').

racemic_mixture(C,N) :-
        ontobee ??
        rdf_path(C,rdfs:subClassOf,'http://purl.obolibrary.org/obo/CHEBI_60911',obomerged:'CHEBI'),
        rdf(C,rdfs:label,N).


zero_charge(A) :-
        rdf(A,'http://purl.obolibrary.org/obo/chebi/charge',Ch),
        {Ch="0"^^xsd:string}.


foo("0").


inchi(C,A) :-
        (   ontobee ?? rdf(C,'http://purl.obolibrary.org/obo/chebi/inchi',S)),
        literal_atom(S,A).

is_enantiomer_of(C1,C2) :-
        subclass_of_some(C1,'http://purl.obolibrary.org/obo/chebi#is_enantiomer_of',C2).

is_conjugate_base_of(C1,C2) :-
        subclass_of_some(C1,'http://purl.obolibrary.org/obo/chebi#is_conjugate_base_of',C2).
is_conjugate_acid_of(C1,C2) :-
        subclass_of_some(C1,'http://purl.obolibrary.org/obo/chebi#is_conjugate_acid_of',C2).

conjugate_non_reciprocal1(C1,C2) :-
        is_conjugate_base_of(C1,C2),
        \+ is_conjugate_acid_of(C2,C1).
conjugate_non_reciprocal2(C1,C2) :-
        is_conjugate_acid_of(C1,C2),
        \+ is_conjugate_base_of(C2,C1).


has_part(C,P,N) :-
        ontobee ??
        subclass_of_some(C,'http://purl.obolibrary.org/obo/BFO_0000051',P),
        rdf(P,rdfs:label,N).

has_lr(C,L,R,Parent) :-
        setof(P-N,(   ontobee ??
                  subclass_of_some(C,'http://purl.obolibrary.org/obo/BFO_0000051',P),
                      rdf(P,rdfs:label,N)),Ps),
        member(L-LN,Ps),
        lit_startswith(LN,'(S)'),
        member(R-RN,Ps),
        lit_startswith(RN,'(R)'),
        (   ontobee ??
        rdf(L,rdfs:subClassOf,Parent,obomerged:'CHEBI'),
        rdf(R,rdfs:subClassOf,Parent,obomerged:'CHEBI')).



lit_startswith(N,A) :-
        literal_atom(N,NA),
        atom_concat(A,_,NA).

acid(A,N) :-
        ontobee ??
        exists(is_conjugate_base_of(_,A)),
        zero_charge(A),
        rdf(A,rdfs:label,N).
acid_base(A,B,BN,Ch) :-
        ontobee ??
        is_conjugate_base_of(B,A),
        rdf(B,'http://purl.obolibrary.org/obo/chebi/charge',Ch),
        rdf(B,rdfs:label,BN).
conjugate(A,B,AN,BN,ACh,BCh) :-
        ontobee ??
        is_conjugate_base_of(B,A),
        chrdf(A,rdfs:label,AN),
        chrdf(A,'http://purl.obolibrary.org/obo/chebi/charge',ACh),
        chrdf(B,rdfs:label,BN),
        chrdf(B,'http://purl.obolibrary.org/obo/chebi/charge',BCh).

conjugate_no_charge1(A,B,AN,BN,ACh) :-
        ontobee ??
        is_conjugate_base_of(B,A),
        chrdf(A,rdfs:label,AN),
        chrdf(A,'http://purl.obolibrary.org/obo/chebi/charge',ACh),
        chrdf(B,rdfs:label,BN),
        \+ chrdf(B,'http://purl.obolibrary.org/obo/chebi/charge',_).
conjugate_no_charge2(A,B,AN,BN,BCh) :-
        ontobee ??
        is_conjugate_base_of(B,A),
        chrdf(A,rdfs:label,AN),
        \+ chrdf(A,'http://purl.obolibrary.org/obo/chebi/charge',_),
        chrdf(B,rdfs:label,BN),
        chrdf(B,'http://purl.obolibrary.org/obo/chebi/charge',BCh).

chrdf(S,P,O) :- rdf(S,P,O,obomerged:'CHEBI').

inchi_search(P,C) :-
        inchi_search(P,C,_).
inchi_search(P,C,S) :-
        chrdf(C,'http://purl.obolibrary.org/obo/chebi/inchi',S),
        contains(str(S),P).

        
enantiomer(C,N,P) :-
        ontobee ??
        subclass_of_some(C,'http://purl.obolibrary.org/obo/chebi#is_enantiomer_of',C2),
        rdf(C,rdfs:label,N),
        rdf(C,rdfs:subClassOf,P),
        rdf(C2,rdfs:subClassOf,P),
        % C2 should be the only child of P
        \+ ((rdf(C3,rdfs:subClassOf,P),
             C3\=C,
             C3\=C2)).

enantiomer_config(C,N,P,Config) :-
        enantiomer(C,N,P),
        literal_atom(N,A),
        concat_atom([Config,_|_],'-',A).



inchi_token(S,Tok) :- concat_atom(Toks,/,S),member(Tok,Toks).
inchi_m(S,X) :- inchi_token(S,X),atom_concat(m,_,X).

inchi_subtract(C1,C2,Diff) :-
        inchi(C1,I1),
        inchi(C2,I2),
        atom_concat(I2,Diff,I1).


dataframe:dataframe(inchi,
                    [[class=C,
                      inchi=I]-inchi(C,I),
                     [m=X]-inchi_m(I,X)],
                    [entity(class),
                     description('All racemic mixtures in CHEBI')]).


dataframe:dataframe(acid,
                    [[class=A,
                      name=N]-acid(A,N),
                     [inchi=AI]-inchi(A,AI),
                     [base=B,base_name=BN,base_charge=Ch]-acid_base(A,B,BN,Ch)
                    ],
                    [description('All acids in CHEBI')]).
dataframe:dataframe(enantiomer,
                    [[class=C,
                      name=N,
                      enantiomer_form_of=P,
                      config=Config]-enantiomer_config(C,N,P,Config),
                     [inchi=CI]-inchi(C,CI),
                     [parent_inchi=PI]-inchi(P,PI),
                     [diff=Diff]-inchi_subtract(C,P,Diff)
                    ],
                    [description('All enantiomers in CHEBI')]).
dataframe:dataframe(racemic_mixture,
                    [[class=C,
                      name=N]-racemic_mixture(C,N),
                     [inchi=Inchi]-inchi(C,Inchi),
                     [left=L,right=R,agnostic=Parent,
                      agnostic_inchi=PInchi,
                      left_inchi=LInchi,
                      right_inchi=RInchi
                     ]-(has_lr(C,L,R,Parent),
                        inchi(Parent,PInchi),
                        inchi(L,LInchi),
                        inchi(R,RInchi))
                    ],
                    [description('All racemic mixtures in CHEBI')]).

dataframe:dataframe(has_part,
                    [[class=C,
                      name=N]-rdf(C,rdfs:label,N),
                     [has_part=P,
                      has_part_name=PN]-has_part(C,P,PN)
                    ],
                    [description('All has_parts')]).
dataframe:dataframe(conjugate,
                    [[acid=A,
                      base=B]-is_conjugate_base_of(A,B)
                    ],
                    [entity(A),
                     entity(B),
                     description('All has_parts')]).

dataframe:dataframe(test,
                    [[x=X]-member(X,[a,b,c])],
                    [endpoint(ontobee)]).


inchi_iri(S,X) :-
        atom_concat('https://w3id.org/chemschema/ChemicalEntity/',S,X).

write_triples(C) :-
        gen_triples(C,Triples),
        forall(member(T,Triples),
               writeln(T)).

%! save_triples(?Cls, +Filename) is det.
%
%   save all triples inferred for chem class Cls to Filename
%
save_triples(C,F) :-
        G=gen,
        forall(gen_triple(C,rdf(S,P,O)),
               (   rdf_assert(S,P,O,G),
                   writeln(rdf(S,P,O)))),
        ensure_loaded(library(semweb/rdf_turtle)),
        rdf_save_turtle(F, [graph(G)]).


gen_triple(C,T) :-
        gen_triples(C,L),
        member(T,L).

gen_triples('RacemicMixture',Triples) :-
        rdf_global_id(chem:'RacemicMixture',RMC),
        Triples=[
                 rdf(I,rdf:type,RMC),
                 rdf(I,rdfs:label,N),
                 rdf(I,chem:chebi_iri,C),
                 rdf(I,chem:has_left_enantiomer,LI),
                 rdf(I,chem:has_right_enantiomer,RI),
                 rdf(I,chem:chirality_agnostic_form,PI)
                 ],
        racemic_mixture(C,N),
        %inchi(C,Inchi),
        has_lr(C,L,R,Parent),
        inchi(Parent,PInchi),
        inchi(L,LInchi),
        inchi(R,RInchi),
        inchi_iri(LInchi,LI),
        inchi_iri(RInchi,RI),
        inchi_iri(PInchi,PI),
        atom_concat(PInchi,'/s3',MInchi),
        inchi_iri(MInchi,I).

gen_triples(foo,[rdf(x,a,y)]).

gen_triples('Enantiomer',Triples) :-
        rdf_global_id(chem:'Enantiomer',Metaclass),
        Triples=[
                 rdf(I,rdf:type,Metaclass),
                 rdf(I,rdfs:label,N),
                 rdf(I,chem:chebi_iri,C),
                 rdf(I,chem:config,literal(Config)),
                 rdf(I,chem:enantiomer_form_of,PI)
                 ],
        enantiomer_config(C,N,Parent,Config),
        inchi(C,Inchi),  % TODO - infer this
        inchi(Parent,PInchi),
        atom_concat(Inchi,InchiDiff,PInchi),
        writeln(diff(InchiDiff,Config)),
        inchi_iri(PInchi,PI),
        inchi_iri(Inchi,I).


        

