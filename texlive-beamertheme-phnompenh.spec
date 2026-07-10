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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a simple theme, similar to some others, but
designed to be attractive.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamertheme-phnompenh
%dir %{_datadir}/texmf-dist/tex/latex/beamertheme-phnompenh
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-phnompenh/README
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-phnompenh/beamerthemePhnomPenh.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-phnompenh/beamerthemePhnomPenh.tex
%{_datadir}/texmf-dist/tex/latex/beamertheme-phnompenh/beamerthemePhnomPenh.sty
