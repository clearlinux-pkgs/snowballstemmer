#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : snowballstemmer
Version  : 1.2.1
Release  : 2
URL      : http://pypi.debian.net/snowballstemmer/snowballstemmer-1.2.1.tar.gz
Source0  : http://pypi.debian.net/snowballstemmer/snowballstemmer-1.2.1.tar.gz
Summary  : This package provides 16 stemmer algorithms (15 + Poerter English stemmer) generated from Snowball algorithms.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: snowballstemmer-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Snowball stemming library collection for Python
===============================================

%package python
Summary: python components for the snowballstemmer package.
Group: Default

%description python
python components for the snowballstemmer package.


%prep
%setup -q -n snowballstemmer-1.2.1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1488568737
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1488568737
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
