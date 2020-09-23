
# Type: reaction participant




URI: [chemont:ReactionParticipant](https://w3id.org/chemont/ReactionParticipant)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ChemicalEntity]<chemical%200..1-%20[ReactionParticipant&#124;stoichiometry:integer%20%3F],[Reaction]++-%20left%20participants%200..*>[ReactionParticipant],[Reaction]++-%20right%20participants%200..*>[ReactionParticipant],[Reaction],[ChemicalEntity])

## Referenced by class

 *  **None** *[left participants](left_participants.md)*  <sub>0..*</sub>  **[ReactionParticipant](ReactionParticipant.md)**
 *  **[Reaction](Reaction.md)** *[reaction➞left participants](reaction_left_participants.md)*  <sub>0..*</sub>  **[ReactionParticipant](ReactionParticipant.md)**
 *  **[Reaction](Reaction.md)** *[reaction➞right participants](reaction_right_participants.md)*  <sub>0..*</sub>  **[ReactionParticipant](ReactionParticipant.md)**
 *  **None** *[right participants](right_participants.md)*  <sub>0..*</sub>  **[ReactionParticipant](ReactionParticipant.md)**

## Attributes


### Own

 * [reaction participant➞chemical](reaction_participant_chemical.md)  <sub>OPT</sub>
    * range: [ChemicalEntity](ChemicalEntity.md)
 * [reaction participant➞stoichiometry](reaction_participant_stoichiometry.md)  <sub>OPT</sub>
    * range: [Integer](types/Integer.md)
