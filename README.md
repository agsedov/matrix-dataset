# matrix-dataset

Annotated handwritten matrix expressions dataset + generator for handout materials.

## Project structure
* Code for handout materials generator in ./generator
* Handwritten pages in ./data/pages
* Matrices extracted by YOLO in ./data/extracted

## Handout materials generator rules.
Generator roughly mimics distribution of matrices in certain linear algebra course.
 * Matrices are filled with integers.
 * 25% of matrices can contain 3-digit numbers, other not.
 * 35% matrices have curly braces (Regular), 35% have curly braces and vertical divider (SLE), 30% have vertical braces (Determinants).
 * Matrices with vertical braces are square with random rank of 2, 3 or 4.
 * SLE matrices can have 2-6 columns. If SLE matrix has N columns, then it can have 2-N rows.
 * Number of rows and columns in regular matrix are independent variables with same distribution: p(k=2)=0.4, p(k=3)=0.3, p(k=4)=0.2, p(k=5)=0.1
