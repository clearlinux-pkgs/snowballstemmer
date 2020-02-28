#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6646265B586B83CB (mitya57@gmail.com)
#
Name     : snowballstemmer
Version  : 2.0.0
Release  : 32
URL      : https://files.pythonhosted.org/packages/21/1b/6b8bbee253195c61aeaa61181bb41d646363bdaa691d0b94b304d4901193/snowballstemmer-2.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/21/1b/6b8bbee253195c61aeaa61181bb41d646363bdaa691d0b94b304d4901193/snowballstemmer-2.0.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/21/1b/6b8bbee253195c61aeaa61181bb41d646363bdaa691d0b94b304d4901193/snowballstemmer-2.0.0.tar.gz.asc
Summary  : This package provides 26 stemmers for 25 languages generated from Snowball algorithms.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: snowballstemmer-license = %{version}-%{release}
Requires: snowballstemmer-python = %{version}-%{release}
Requires: snowballstemmer-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
It includes following language algorithms:

* Arabic
* Basque
* Catalan
* Danish
* Dutch
* English (Standard, Porter)
* Finnish
* French
* German
* Greek
* Hindi
* Hungarian
* Indonesian
* Irish
* Italian
* Lithuanian
* Nepali
* Norwegian
* Portuguese
* Romanian
* Russian
* Spanish
* Swedish
* Tamil
* Turkish

This is a pure Python stemming library. If `PyStemmer <https://pypi.org/project/PyStemmer/>`_ is available, this module uses
it to accelerate.

%package license
Summary: license components for the snowballstemmer package.
Group: Default

%description license
license components for the snowballstemmer package.


%package python
Summary: python components for the snowballstemmer package.
Group: Default
Requires: snowballstemmer-python3 = %{version}-%{release}

%description python
python components for the snowballstemmer package.


%package python3
Summary: python3 components for the snowballstemmer package.
Group: Default
Requires: python3-core
Provides: pypi(snowballstemmer)

%description python3
python3 components for the snowballstemmer package.


%prep
%setup -q -n snowballstemmer-2.0.0
cd %{_builddir}/snowballstemmer-2.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582921175
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/snowballstemmer
cp %{_builddir}/snowballstemmer-2.0.0/COPYING %{buildroot}/usr/share/package-licenses/snowballstemmer/3938505906e841002141cb01bbda1e971614e34a
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/snowballstemmer/3938505906e841002141cb01bbda1e971614e34a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
