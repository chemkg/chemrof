
# Type: reaction


reaction

URI: [chemont:Reaction](https://w3id.org/chemont/Reaction)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ReactionParticipant],[ReactionParticipant]<right%20participants%200..*-++[Reaction&#124;direction:string%20%3F;smarts_string:string%20%3F;is_stereo:boolean%20%3F;is_balanced:boolean%20%3F;is_transport:boolean%20%3F;is_fully_characterized:boolean%20%3F;reaction_center:string%20%3F;description:string%20%3F],[ReactionParticipant]<left%20participants%200..*-++[Reaction])

## Referenced by class


## Attributes


### Own

 * [reaction➞description](reaction_description.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [reaction➞direction](reaction_direction.md)  <sub>OPT</sub>
    * Description: One of l->r, r->l, bidirectional, neutral
    * range: [String](types/String.md)
 * [reaction➞is balanced](reaction_is_balanced.md)  <sub>OPT</sub>
    * range: [Boolean](types/Boolean.md)
 * [reaction➞is fully characterized](reaction_is_fully_characterized.md)  <sub>OPT</sub>
    * Description: False if includes R-groups
    * range: [Boolean](types/Boolean.md)
 * [reaction➞is stereo](reaction_is_stereo.md)  <sub>OPT</sub>
    * range: [Boolean](types/Boolean.md)
 * [reaction➞is transport](reaction_is_transport.md)  <sub>OPT</sub>
    * range: [Boolean](types/Boolean.md)
 * [reaction➞left participants](reaction_left_participants.md)  <sub>0..*</sub>
    * range: [ReactionParticipant](ReactionParticipant.md)
 * [reaction➞reaction center](reaction_reaction_center.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [reaction➞right participants](reaction_right_participants.md)  <sub>0..*</sub>
    * range: [ReactionParticipant](ReactionParticipant.md)
 * [reaction➞smarts string](reaction_smarts_string.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
