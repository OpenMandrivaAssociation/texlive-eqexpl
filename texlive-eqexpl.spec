Name:		texlive-eqexpl
Version:	63629
Release:	1
Summary:	Align explanations for formulas
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eqexpl
License:	cc-by-sa-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqexpl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqexpl.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package was developed in response to a question on
https://tex.stackexchange.com. Its purpose is to enable a
perfectly formatted explanation of components of a formula. The
package depends on calc, etoolbox, and xparse.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/eqexpl
%doc %{_texmfdistdir}/doc/latex/eqexpl

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
