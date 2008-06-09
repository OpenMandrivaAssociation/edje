%define	name edje
%define	version 0.9.9.043
%define release %mkrel 1

%define major 0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary: 	Complex graphical design & layout library
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://www.enlightenment.org/
Source: 	http://download.enlightenment.org/snapshots/LATEST/%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires: 	embryo-devel => 0.9.1.042
BuildRequires:	ecore-devel => 0.9.9.042

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
%_datadir/%name

%files -n %libname
%defattr(-,root,root)
%_libdir/lib*.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root)
%_libdir/lib*.so
%_libdir/lib*.*a
%_libdir/pkgconfig/*.pc
%_includedir/*.h
