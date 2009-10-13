%bcond_with	tests # broken
#
%define 	module	pyliblzma
Summary:	Platform independent python bindings for the LZMA compression library
Name:		python-%{module}
Version:	0.5.2
Release:	1
License:	LGPL v3
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/p/pyliblzma/%{module}-%{version}.tar.bz2
# Source0-md5:	8e5596bc60e784c74f10e94820655336
URL:		https://launchpad.net/pyliblzma
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	xz-devel
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PylibLZMA provides a python interface for the liblzma library to read
and write data that has been compressed or can be decompressed by
Lasse Collin's xz / lzma utils.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build \
	--debug

%if %{with tests}
python setup.py test
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_comp $RPM_BUILD_ROOT
%py_ocomp $RPM_BUILD_ROOT
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README THANKS
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py[co]
%{py_sitedir}/pyliblzma-*.egg-info
