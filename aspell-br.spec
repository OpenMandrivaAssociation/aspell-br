%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define ver_major 0.60
%define ver_minor 2

%define src_ver %ver_major-%ver_minor

%define languageenglazy Breton
%define languagecode br
%define lc_ctype br_FR

Summary:       %{languageenglazy} files for aspell
Summary(br):   Geriadur brezhonek evit aspell
Name:          aspell-%{languagecode}
Version:       %ver_major.%ver_minor
Release:       %mkrel 2
Group:         System/Internationalization
Source:        ftp://ftp.gnu.org/gnu/aspell/aspell-%{languagecode}-%{src_ver}.tar.bz2
URL:           http://aspell.net/
License:	   GPL
Provides: spell-br


BuildRequires: aspell >= 0.50
BuildRequires: make
Requires:      aspell >= 0.50

# Mandriva Stuff
Requires:      locales-%{languagecode}
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%description -l br
Geriadur brezhonek evit aspell.

%prep
%setup -q -n %{name}-%{src_ver}

%build

# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

mv -f README README.%{languagecode}
chmod 644 Copyright README.%{languagecode} doc/*

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.%{languagecode} Copyright doc/*
%{_libdir}/aspell-*/*


