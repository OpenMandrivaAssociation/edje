%define	name	edje
%define	version 0.5.0.038
%define release %mkrel 1

%define major 	0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: 	Edje is a complex graphical design & layout library
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://www.get-e.org/
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Buildrequires: 	embryo-devel, ecore-devel >= 0.9.9
BuildRequires:	multiarch-utils autoconf2.5

%description
A graphical layout and animation library for animated resizable, compressed
and scalable themes.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %libname
Summary: Libraries for the edje package
Group: System/Libraries

%description -n %libname
Libraries for edje.

%package -n %libnamedev
Summary: Enlightenment edje headers and development libraries
Group: Development/Other
Requires: %libname = %version
Provides: lib%{name}-devel = %version-%release
Provides: %{name}-devel = %version-%release

%description -n %libnamedev
Edje development headers and libraries.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%multiarch_binaries %buildroot/%_bindir/%name-config

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README 
%_bindir/%{name}_*
%_datadir/%name

%files -n %libname
%defattr(-,root,root)
%_libdir/lib*.so.*

%files -n %libnamedev
%defattr(-,root,root)
%_libdir/lib*.so
%_libdir/lib*.*a
%_libdir/pkgconfig/*.pc
%_includedir/*.h
%_bindir/%name-config
%multiarch %multiarch_bindir/%name-config



%changelog
* Wed May 16 2007 Antoine Ginies <aginies@mandriva.com> 0.5.0.038-1mdv2008.0
- CVS snapshot 20070516

* Tue Apr 24 2007 Pascal Terjan <pterjan@mandriva.org> 0.5.0.037-2mdv2008.0
+ Revision: 17719
- Rebuild with the new ecore

* Mon Apr 23 2007 Pascal Terjan <pterjan@mandriva.org> 0.5.0.037-1mdv2008.0
+ Revision: 17694
- New snapshot
- Use autoconf2.5
- Import edje



* Mon Aug 07 2006 Lenny Cartier <lenny@mandriva.com> 0.5.0.025-0.20060323.2mdv2007.0
- rebuild

* Fri Mar 24 2006 Austin Acton <austin@mandriva.org> 0.5.0.025-0.20060323.1mdk
- new cvs checkout

* Fri Feb 17 2006 Austin Acton <austin@mandriva.org> 0.5.0.023-0.20060216.1mdk
- new cvs checkout

* Wed Jan 18 2006 Austin Acton <austin@mandriva.org> 0.5.0.023-0.20060117.1mdk
- new cvs checkout

* Fri Nov 25 2005 Austin Acton <austin@mandriva.org> 0.5.0.019-0.20051124.1mdk
- new cvs checkout

* Wed Nov 09 2005 Austin Acton <austin@mandriva.org> 0.5.0.018-0.20051109.1mdk
- new cvs checkout

* Sat Nov 05 2005 Austin Acton <austin@mandriva.org> 0.5.0.018-0.20051104.1mdk
- new cvs checkout

* Mon Sep 05 2005 Austin Acton <austin@mandriva.org> 0.5.0.013-0.20050904.1mdk
- new cvs checkout

* Sun Aug 14 2005 Austin Acton <austin@mandriva.org> 0.5.0.013-0.20050813.1mdk
- new cvs checkout

* Mon Jun 27 2005 Austin Acton <austin@mandriva.org> 0.5.0.010-0.20050627.1mdk
- new cvs checkout

* Wed Jun 08 2005 Austin Acton <austin@mandriva.org> 0.5.0.008-0.20050608.1mdk
- new cvs checkout

* Wed May 25 2005 Austin Acton <austin@mandriva.org> 0.5.0.007-0.20050524.3mdk
- multiarch binaries

* Wed May 25 2005 Austin Acton <austin@mandriva.org> 0.5.0.007-0.20050524.2mdk
- more fixes

* Wed May 25 2005 Austin Acton <austin@mandriva.org> 0.5.0.007-0.20050524.1mdk
- new cvs checkout
- tidy spec

* Fri Sep 24 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.5.0-0.20040913.2mdk
- add some requires exceptions
- fix libedje-devel requires 

* Fri Sep 24 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.5.0-0.20040913.1mdk
- 0.5.0 20040913
