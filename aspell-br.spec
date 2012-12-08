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
Release:       %mkrel 12
Group:         System/Internationalization
Source:        ftp://ftp.gnu.org/gnu/aspell/aspell-%{languagecode}-%{src_ver}.tar.bz2
URL:           http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-br


BuildRequires: aspell >= 0.50
BuildRequires: make
Requires:      aspell >= 0.50

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
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




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.60.2-10mdv2011.0
+ Revision: 662800
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 0.60.2-9mdv2011.0
+ Revision: 603195
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.60.2-8mdv2010.1
+ Revision: 518909
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.60.2-7mdv2010.0
+ Revision: 413049
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.60.2-6mdv2009.1
+ Revision: 350001
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.60.2-5mdv2009.0
+ Revision: 220364
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.60.2-4mdv2008.1
+ Revision: 182403
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.60.2-3mdv2008.1
+ Revision: 148741
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.60.2-2mdv2007.0
+ Revision: 123227
- Import aspell-br

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.60.2-2mdv2007.1
- use the mkrel macro
- disable debug packages

* Wed May 18 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.60.2-1mdk
- accept "'" as ellidation mark at end of words (eg "gan' an dud")

* Fri May 13 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.60.1-1mdk
- update word list:
  o add muted words
  o add conjugued verbs
- accept "'" as ellidation mark at beginning of words

* Fri Dec 03 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.50.2-6mdk
- rebuild for new aspell

* Wed Jul 28 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.50.2-5mdk
- allow build on ia64

