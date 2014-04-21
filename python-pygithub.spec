%define 	module	PyGithub

Summary:	Python library implementing the full Github API v3
Name:		python-%{module}
Version:	1.24.1
Release:	1
License:	GPL v3 / LGPL v3
Group:		Development/Languages/Python
Source0:	https://github.com/jacquev6/PyGithub/archive/v%{version}.tar.gz
# Source0-md5:	498cd382371535a4289c07b5db4d52b8
URL:		http://jacquev6.github.io/PyGithub/v1/index.html
BuildRequires:	python-modules
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Python 2 library to access the Github API v3.
With it, you can manage Github resources (repositories, user profiles,
organizations, etc.) from Python scripts.

%package -n python3-%{module}
Summary:	Python library implementing the full Github API v3
Group:		Development/Languages/Python
Requires:	python3-modules

%description -n python3-%{module}
This is a Python 3 library to access the Github API v3.
With it, you can manage Github resources (repositories, user profiles,
organizations, etc.) from Python scripts.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build -b python
%{__python3} setup.py build -b python3

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py build -b python install \
	--optimize=2		\
	--root=$RPM_BUILD_ROOT	\
	--skip-build

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%{__python3} setup.py build -b python3 install \
	--optimize=2		\
	--root=$RPM_BUILD_ROOT	\
	--skip-build

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/github/tests
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/github/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%%doc
#%%attr(755,root,root) %{_bindir}/*
%dir %{py_sitescriptdir}/github
%{py_sitescriptdir}/github/*.py[co]
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info

%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/github
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
