%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define ver_major 0.60
%define ver_minor 2

%define src_ver %ver_major-%ver_minor

%define languageenglazy Breton
%define languagecode br
%define lc_ctype br_FR

Summary:	%{languageenglazy} files for aspell
Summary(br):	Geriadur brezhonek evit aspell
Name:		aspell-%{languagecode}
Version:	%ver_major.%ver_minor
Release:	17
Group:		System/Internationalization
License:	GPLv2
Url:		http://aspell.net/
Source0:	ftp://ftp.gnu.org/gnu/aspell/aspell-%{languagecode}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= 0.50
Requires:	aspell >= 0.50
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}
Provides:	spell-br
Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%description -l br
Geriadur brezhonek evit aspell.

%prep
%setup -qn %{name}-%{src_ver}

%build

# don't use configure macro
./configure

%make

%install
%makeinstall_std

mv -f README README.%{languagecode}
chmod 644 Copyright README.%{languagecode} doc/*

%files
%doc README.%{languagecode} Copyright doc/*
%{_libdir}/aspell-*/*

