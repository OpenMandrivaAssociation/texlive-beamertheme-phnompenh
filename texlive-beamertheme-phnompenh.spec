%global tl_name beamertheme-phnompenh
%global tl_revision 39100

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A simple beamer theme
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/phnompenh
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-phnompenh.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-phnompenh.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a simple theme, similar to some others, but
designed to be attractive.

