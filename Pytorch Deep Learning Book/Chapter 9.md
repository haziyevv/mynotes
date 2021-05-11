# Chapter 9

**Voxel**: 3d equivalent of a pixel. Arranged in a 3d grid to represent a field of data. Each **Voxel** of a **CT** scan corresponds to the average mass density of the matter contained inside.  High density material like **bones and metal implants** will be shown as **white**, low density **air and lung tissue** as **black** and fat and tissue as various shades of gray.

End to end solution process:

1) Load CT data files to produce a CT instance that contains the full 3D scan.

2) Identify voxels of potential tumors. Like a heatmap.

3) Group the interesting voxels into small **lumps**.
4. Identify nodules. Classify candidate nodules as a nodule or not.  

5. Find if the nodules are actually malignant. 

**Tumor** : Mass of tissue made of proliferating cells in the lung is a tumor.

**Nodule:** A small tumor (just a few millimeters wide) in the lung is called a nodule. 

# Chapter 10

1. setdefault(key, "Something else") --> returns the value of the given key if it exists else returns the given default.

```
person = {"name":"Farid", "surname":"Haziyev"}


print(person.setdefault("father_name", "Faiq"))

--> Faiq
```

2. namedtuple --> collection in python. A container like dictionary but in tupple format, but can be used as key value pair and are iterable.

```
from collections import namedtuple


CandidateInfoTuple = namedtuple(
    'CandidateInfoTuple',
    'isNodule_bool, diameter_mm, series_uid, center_xyz',
)


--> first string is the name
--> others are keys


candidateInfo_list.append(CandidateInfoTuple(
                isNodule_bool,
                candidateDiameter_mm,
                series_uid,
                candidateCenter_xyz,
               ))
```

3. for else in python. If iteration does not break out of the for loop the it will enter to else statement.

4. **DICOM** --> native file format for ct scans.

5. **Hounsfield scale** quantitative scale used for radiodensity. Frequently used on ct scans. 
