Name:		python-gunicorn
Version:	23.0.0
Release:	1
Summary:	Python WSGI HTTP server, Frappe fork
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/gunicorn/
Source0:	gunicorn-54b59ca.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch
%description
Python WSGI HTTP server, Frappe fork.

%files
%{py_sitedir}/*
%{_bindir}/*
