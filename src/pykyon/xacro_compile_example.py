from adarl.utils.base_utils import compile_xacro_string, pkgutil_get_path
from pathlib import Path

model_path = pkgutil_get_path("pykyon", "iit-kyon-ros-pkg/kyon_urdf/urdf/kyon.urdf.xacro")
urdf_string = compile_xacro_string( model_definition_string=Path(model_path).read_text(),
                                    model_kwargs={},
                                    extra_pkg_paths={   "kyon_urdf" : pkgutil_get_path("pykyon", "iit-kyon-ros-pkg/kyon_urdf")})
print(urdf_string)