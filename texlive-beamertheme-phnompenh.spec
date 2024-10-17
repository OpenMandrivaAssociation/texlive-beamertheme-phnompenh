Name:		texlive-beamertheme-phnompenh
Version:	39100
Release:	2
Summary:	A simple beamer theme
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamertheme-phnompenh
License:	gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-phnompenh.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-phnompenh.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a simple theme, similar to some others,
but designed to be attractive.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/beamertheme-phnompenh
%doc %{_texmfdistdir}/doc/latex/beamertheme-phnompenh

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
