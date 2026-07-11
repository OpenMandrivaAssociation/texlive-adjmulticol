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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package adds, to the multicol package, the option to change the
margins for multicolumn and unicolumn layout. The package understands
the difference between the even and odd margins for two side printing.

