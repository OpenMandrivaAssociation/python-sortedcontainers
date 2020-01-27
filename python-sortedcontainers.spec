%define module	sortedcontainers

Name:           python-%{module}
Version:        2.1.0
Release:        %mkrel 2
Group:          Development/Python
Summary:        Sorted container data types
License:        ASL2.0
URL:            https://pypi.python.org/pypi/sortedcontainers
Source0:        https://pypi.python.org/packages/source/s/sortedcontainers/sortedcontainers-%{version}.tar.gz
BuildArch:      noarch

%description
SortedContainers is an Apache2 licensed containers library, written in
pure-Python, and fast as C-extensions.

%package -n     python3-%{module}
Summary:        Sorted container data types
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
%{?python_provide:%python_provide python3-%{module}}

%description -n python3-%{module}
SortedContainers is an Apache2 licensed containers library, written in
pure-Python, and fast as C-extensions.

%prep
%setup -q -n %{module}-%{version}

# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{module}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-%{version}-py?.?.egg-info