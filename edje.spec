%define	name edje
%define	version 1.0.0
%define release %mkrel -c beta3 1

%define major 1
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary: 	Complex graphical design & layout library
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://www.enlightenment.org/
Source: 	http://download.enlightenment.org/releases/%{name}-%{version}.beta3.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires: 	embryo-devel => 1.0.0
BuildRequires:	ecore-devel => 1.0.0
BuildRequires:	lua-devel

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
%setup -qn %{name}-%{version}.beta3

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README 
%_bindir/%{name}_*
%_bindir/inkscape2edc
%_datadir/%name
%_datadir/mime/packages/edje.xml

%files -n %libname
%defattr(-,root,root)
%_libdir/lib*.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root)
%_libdir/lib*.so
%_libdir/lib*.*a
%_libdir/pkgconfig/*.pc
%_includedir/*
