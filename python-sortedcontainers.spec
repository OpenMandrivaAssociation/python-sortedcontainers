%define module	sortedcontainers

Name:           python-%{module}
Version:        2.1.0
Release:        1
Group:          Development/Python
Summary:        Sorted container data types
License:        ASL2.0
URL:            https://pypi.python.org/pypi/sortedcontainers
Source0:        https://pypi.python.org/packages/source/s/sortedcontainers/sortedcontainers-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)
%{?python_provide:%python_provide python-%{module}}

%description
SortedContainers is an Apache2 licensed containers library, written in
pure-Python, and fast as C-extensions.

%prep
%setup -q -n %{module}-%{version}

# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}-py?.?.egg-info
