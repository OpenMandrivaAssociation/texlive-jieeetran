Name:		texlive-jieeetran
Version:	65642
Release:	1
Summary:	UnofficiaL BibTeX style for citing Japanese articles in IEEE format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jieeetran
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jieeetran.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jieeetran.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an unofficial BibTeX style for authors
trying to cite Japanese articles in the Institute of Electrical
and Electronics Engineers (IEEE) format.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/bibtex/bst/jieeetran
%doc %{_texmfdistdir}/doc/bibtex/jieeetran

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
