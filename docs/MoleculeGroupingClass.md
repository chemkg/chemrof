
# Type: molecule grouping class


A grouping class that classifies molecules. Example: carbohydrate, monosaccharide, amino acid, alkane(?)

URI: [chemont:MoleculeGroupingClass](https://w3id.org/chemont/MoleculeGroupingClass)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Molecule]<classifies%200..1-%20[MoleculeGroupingClass],[GroupingClass]^-[MoleculeGroupingClass],[Molecule],[GroupingClass])

## Parents

 *  is_a: [GroupingClass](GroupingClass.md) - A non-specific entity. For example "amino acid" is a grouping for "serine", "leucine" etc; ester is a grouping for nitroglycerin; alkane is a grouping for pentane, butane, methane, etc

## Referenced by class


## Attributes


### Own

 * [molecule grouping class➞classifies](molecule_grouping_class_classifies.md)  <sub>OPT</sub>
    * range: [Molecule](Molecule.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | Unlike an actual molecule, a molecule grouping class will not have an inchi or properties such as mass |
|  | | {'TODO': 'decide if alkane which has a generic formula belongs here'} |

