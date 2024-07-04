Lists a breakdown of what makes up the size of a .blend file.

```shell
# arguments: <path-to-blend-file> <size-threshold-in-mb>
# example:
python3 main.py file.blend 0.01
```

---

Example output:

```
DATA: 20.00 MB
BR: 0.16 MB
DNA1: 0.12 MB
ME: 0.08 MB
OB: 0.06 MB
TEST: 0.06 MB
----------------------
Total: 20.53 MB

TEST
  DrawDataList: 0.06 MB
DATA
  MIntProperty: 4.57 MB
  vec2f: 3.92 MB
  MDeformVert: 2.48 MB
  vec2i: 2.42 MB
  vec2s: 1.96 MB
  vec3f: 1.86 MB
  DrawDataList: 1.73 MB
  bNodeSocket: 0.45 MB
  CurveMapping: 0.18 MB
  ARegion: 0.10 MB
  CustomDataLayer: 0.08 MB
  SpaceImage: 0.04 MB
  bNode: 0.02 MB
  Panel: 0.02 MB
  IDProperty: 0.02 MB
  View3D: 0.02 MB
  CurveMapPoint: 0.01 MB
  bNodeTree: 0.01 MB
  SeqTimelineChannel: 0.01 MB
  RegionView3D: 0.01 MB
BR
  Brush: 0.16 MB
OB
  Object: 0.06 MB
ME
  Mesh: 0.08 MB
DNA1
  DrawDataList: 0.12 MB
```