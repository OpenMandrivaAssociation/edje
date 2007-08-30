%define	name edje
%define	version 0.5.0.038
%define release %mkrel 6

%define major 0
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
Buildrequires: 	embryo-devel >= 0.9.1.038, ecore-devel >= 0.9.9
BuildRequires:	multiarch-utils autoconf2.5

%description
A graphical layout and animation library for animated resizable, compressed
and scalable themes.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %libname
Summary: Libraries for the edje package
Group: System/Libraries
provides: %libname = %version-%release

%description -n %libname
Libraries for edje.

%package -n %libnamedev
Summary: Enlightenment edje headers and development libraries
Group: Development/Other
Requires: %libname = %version
Provides: %{libname}-devel = %version-%release
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


