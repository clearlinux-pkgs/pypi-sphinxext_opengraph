#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-sphinxext_opengraph
Version  : 0.5.1
Release  : 5
URL      : https://files.pythonhosted.org/packages/9d/86/d15957e0d2f3a4ab3ef0376365e1a9cff797dddcae71f3ceb35438f7c363/sphinxext-opengraph-0.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/9d/86/d15957e0d2f3a4ab3ef0376365e1a9cff797dddcae71f3ceb35438f7c363/sphinxext-opengraph-0.5.1.tar.gz
Summary  : Sphinx Extension to enable OGP support
Group    : Development/Tools
License  : MIT
Requires: pypi-sphinxext_opengraph-python = %{version}-%{release}
Requires: pypi-sphinxext_opengraph-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(sphinx)

%description
# sphinxext-opengraph
![Build](https://github.com/wpilibsuite/sphinxext-opengraph/workflows/Test%20and%20Deploy/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

%package python
Summary: python components for the pypi-sphinxext_opengraph package.
Group: Default
Requires: pypi-sphinxext_opengraph-python3 = %{version}-%{release}

%description python
python components for the pypi-sphinxext_opengraph package.


%package python3
Summary: python3 components for the pypi-sphinxext_opengraph package.
Group: Default
Requires: python3-core
Provides: pypi(sphinxext_opengraph)
Requires: pypi(sphinx)

%description python3
python3 components for the pypi-sphinxext_opengraph package.


%prep
%setup -q -n sphinxext-opengraph-0.5.1
cd %{_builddir}/sphinxext-opengraph-0.5.1
pushd ..
cp -a sphinxext-opengraph-0.5.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656370336
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
