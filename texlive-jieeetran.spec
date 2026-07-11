%global tl_name jieeetran
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.19
Release:	%{tl_revision}.1
Summary:	Unofficial BibTeX style for citing Japanese articles in IEEE format
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/jieeetran
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jieeetran.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jieeetran.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides an unofficial BibTeX style for authors trying to
cite Japanese articles in the Institute of Electrical and Electronics
Engineers (IEEE) format.

