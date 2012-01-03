# revision 21512
# category Package
# catalog-ctan /macros/latex/contrib/adjmulticol
# catalog-date 2011-02-24 09:45:27 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-adjmulticol
Version:	1.0
Release:	2
Summary:	Adjusting margins for multicolumn and single column output
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/adjmulticol
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adjmulticol.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adjmulticol.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adjmulticol.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
package extends the multicol package with the option to change
the margins for multicolumn and unicolumn layout. The package
understands the difference between the even and odd margins for
two side printing.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/adjmulticol/adjmulticol.sty
%doc %{_texmfdistdir}/doc/latex/adjmulticol/Makefile
%doc %{_texmfdistdir}/doc/latex/adjmulticol/README
%doc %{_texmfdistdir}/doc/latex/adjmulticol/adjmulticol.bib
%doc %{_texmfdistdir}/doc/latex/adjmulticol/adjmulticol.pdf
%doc %{_texmfdistdir}/doc/latex/adjmulticol/sample.pdf
%doc %{_texmfdistdir}/doc/latex/adjmulticol/sample.tex
#- source
%doc %{_texmfdistdir}/source/latex/adjmulticol/adjmulticol.dtx
%doc %{_texmfdistdir}/source/latex/adjmulticol/adjmulticol.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
