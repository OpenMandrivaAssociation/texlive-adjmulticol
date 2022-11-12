Name:		texlive-adjmulticol
Version:	63320
Release:	1
Summary:	Adjusting margins for multicolumn and single column output
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/adjmulticol
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adjmulticol.r63320.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adjmulticol.doc.r63320.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adjmulticol.source.r63320.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
