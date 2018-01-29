with import <nixpkgs> {};
with pkgs.python36Packages;

buildPythonPackage{
    name = "GBM";
    buildInputs = [ python36Full
                    python36Packages.matplotlib
                    python36Packages.setuptools
                    python36Packages.httplib2
                    python36Packages.urllib3
                    python36Packages.numpy
                    python36Packages.pandas
                    python36Packages.requests
                    python36Packages.joblib
                    python36Packages.quandl
                   ]; 

}

