
Summary: Additional plugins for libtunepimp 
Name:    libtunepimp-extras-freeworld
Version: 0.5.3
Release: 6%{?dist}

License: LGPLv2+
Group: 	 System Environment/Libraries
URL:     http://www.musicbrainz.org/products/tunepimp/
# see http://musicbrainz.org/doc/libtunepimpDownload
Source0: http://ftp.musicbrainz.org/pub/musicbrainz/libtunepimp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# obsolete old livna package
Provides:       libtunepimp-extras-nonfree = %{version}-%{release}
Obsoletes:      libtunepimp-extras-nonfree < 0.5.3-5

Patch1: libtunepimp-0.5.3-gcc43.patch
Patch2: libtunepimp-0.5.3-libmad.patch

%define pkglibdir %{_libdir}/tunepimp

BuildRequires: automake libtool
BuildRequires: libmusicbrainz-devel >= 2.1.0
BuildRequires: readline-devel ncurses-devel
BuildRequires: zlib-devel
BuildRequires: libofa-devel
# These two are likely bogus (used just in examples/ ) -- Rex
BuildRequires: curl-devel
BuildRequires: expat-devel

BuildRequires: libmad-devel

%if 0%{?_with_mp4:1}
BuildRequires: libmp4v2-devel
Provides:  libtunepimp-mp4 = %{version}-%{release}
%endif

Obsoletes: libtunepimp-mp3 < %{version}-%{release}
Provides:  libtunepimp-mp3 = %{version}-%{release}

# Fedora's libtunepimp-0.5.x now Provides: libtunepimp5
Requires: libtunepimp5


%description
%{summary}.


%prep
%setup -q -n libtunepimp-%{version}

%patch1 -p1 -b .gcc43
%patch2 -p1 -b .libmad

libtoolize --force
aclocal
automake


%build
%configure \
  --disable-static \
  --disable-dependency-tracking 

make %{?_smp_mflags} PLUGIN_DIR=%{pkglibdir}/plugins


%check
# sanity check
make -C plugins/mp3 PLUGIN_DIR=%{pkglibdir}/plugins
%{?_with_mp4:make -C plugins/mp4 PLUGIN_DIR=%{pkglibdir}/plugins}


%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT PLUGIN_DIR=%{pkglibdir}/plugins

# delete/omit everything but the mp3 plugin
rm -rf $RPM_BUILD_ROOT%{_bindir}
rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -f  $RPM_BUILD_ROOT%{_libdir}/lib*
rm -f  $RPM_BUILD_ROOT%{pkglibdir}/plugins/[a-l,n-z]*.tpp
rm -f  $RPM_BUILD_ROOT%{pkglibdir}/plugins/m[a-o,q-z]*.tpp
rm -f  $RPM_BUILD_ROOT%{pkglibdir}/plugins/mp[a-z]*.tpp
%{!?_with_mp4:rm -f  $RPM_BUILD_ROOT%{pkglibdir}/plugins/mp4.tpp}


%clean
rm -rf $RPM_BUILD_ROOT


%files 
%defattr(-,root,root,-)
%doc README.LGPL COPYING
%{pkglibdir}/plugins/mp3.tpp
%{?_with_mp4:%{pkglibdir}/plugins/mp4.tpp}


%changelog
* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.5.3-6
- rebuild for new F11 features

* Sun Aug 10 2008 Thorsten Leemhuis <fedora at leemhuis.info> 0.5.3-5
- rename to libtunepimp-extras-freeworld
- add provides and obsoletes for package from livna

* Thu Feb 21 2008 Rex Dieter <rdieter@fedoraproject.org> 0.5.3-4
- gcc43 patch

* Thu Feb 21 2008 Rex Dieter <rdieter@fedoraproject.org> 0.5.3-3
- omit mp4 plugin

* Fri Oct 26 2007 Rex Dieter <rdieter[AT]fedoraprojecg.org> 0.5.3-2
- respin for f8
- License: LGPLv2+

* Wed Nov 29 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.5.3-1
- libtunepimp-0.5.3

* Mon Oct 02 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.5.2-1
- libtunepimp-0.5.2

* Tue Sep 23 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.5.1-1
- libtunepimp-0.5.1

* Wed Sep 20 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.4.3-4
- -mp3 -> -extras-nonfree
- --with-mp4 (BR: libmp4v2-devel)

* Thu Aug 31 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.4.3-2
- BR: taglib-devel readline-devel ncurses-devel
- _with_mp4: include mp4 bits via libmp4v2 (optional, not included by default)

* Tue Aug 29 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.4.3-1
- 0.4.3

* Thu Mar 16 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.4.2-1
- 0.4.2

* Thu Mar 16 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.4.0-3
- gcc41 patch

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Sat Nov 19 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.4.0-0.lvn.2
- BR: libmusicbrainz -> libmusicbrainz-devel
- BR: libogg-devel -> libvorbis-devel
- BR: zlib-devel

* Thu Nov 17 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.4.0-0.lvn.1
- 0.4.0

* Mon Jun 13 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.3.0-1
- gcc4 patch
- 0.3.0 (first try)

