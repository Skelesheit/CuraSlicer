import unittest
from slicertools.utils import convert_3d

from dataclasses import asdict
from slicertools.enums import QualitySlice
from slicertools import materials
from slicertools.slicers import CuraSlicer

examples_convert_3d = {
    'D:/STL/lpwkull_2.stl': './lpwkull_2.stl',
    'D:/STL/xyzCalibration_cube.stl': './xyzCalibration_cube.stl'
}

engine_path = r'D:\UltiMaker Cura 5.7.2\CuraEngine.exe'


class TestConvert3d(unittest.TestCase):

    def test_convert_3d(self):
        for input_path, expected_path in examples_convert_3d.items():
            self.assertEqual(convert_3d(input_path), expected_path)
            print(expected_path)


class TestSlicer(unittest.TestCase):
    def test_slicer(self):
        slicer = CuraSlicer(engine_path=engine_path)
        # проверим все материалы и качество
        result = slicer.slice('D:/STL/xyzCalibration_cube.stl', materials.PETG(), **asdict(QualitySlice.STANDARD))
        self.assertEqual((result.print_time, result.volume), (2891, 4645.0))
        print(f'Slice result:\n{result}')

        result = slicer.slice('D:/STL/xyzCalibration_cube.stl', materials.PETG(), **asdict(QualitySlice.HIGH_QUALITY))
        self.assertEqual((result.print_time, result.volume), (2261, 4626.0))
        print(f'Slice result:\n{result}')
