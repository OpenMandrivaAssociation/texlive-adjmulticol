%global tl_name adjmulticol
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	Adjusting margins for multicolumn and single column output
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/adjmulticol
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adjmulticol.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adjmulticol.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adjmulticol.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package adds, to the multicol package, the option to change the
margins for multicolumn and unicolumn layout. The package understands
the difference between the even and odd margins for two side printing.

%prep
%setup -q -c -a1 -a2
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
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/adjmulticol
%dir %{_datadir}/texmf-dist/source/latex/adjmulticol
%dir %{_datadir}/texmf-dist/tex/latex/adjmulticol
%doc %{_datadir}/texmf-dist/doc/latex/adjmulticol/README
%doc %{_datadir}/texmf-dist/doc/latex/adjmulticol/adjmulticol.bib
%doc %{_datadir}/texmf-dist/doc/latex/adjmulticol/adjmulticol.pdf
%doc %{_datadir}/texmf-dist/doc/latex/adjmulticol/sample.pdf
%doc %{_datadir}/texmf-dist/doc/latex/adjmulticol/sample.tex
%doc %{_datadir}/texmf-dist/source/latex/adjmulticol/Makefile
%doc %{_datadir}/texmf-dist/source/latex/adjmulticol/adjmulticol.dtx
%doc %{_datadir}/texmf-dist/source/latex/adjmulticol/adjmulticol.ins
%{_datadir}/texmf-dist/tex/latex/adjmulticol/adjmulticol.sty
