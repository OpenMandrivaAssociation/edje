%define	major	1
%define	libname %mklibname %{name} %{major}
%define	devname %mklibname %{name} -d

Summary:	Complex graphical design & layout library
Name:		edje
Version:	1.7.8
Release:	1
License:	BSD
Group:		Graphical desktop/Enlightenment
Url:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.fr/releases/%{name}-%{version}.tar.bz2
BuildRequires:	lua-devel
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(ecore-evas)
BuildRequires:	pkgconfig(ecore-file)
BuildRequires:	pkgconfig(ecore-input)
BuildRequires:	pkgconfig(eet)
BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(eio)
BuildRequires:	pkgconfig(embryo)
BuildRequires:	pkgconfig(evas)
Conflicts:	%{libname} < 1.1.99.66793-0.20120103.1
Requires:	evas

%description
A graphical layout and animation library for animated resizable, compressed
and scalable themes.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %{libname}
Summary:	Libraries for the edje package
Group:		System/Libraries

%description -n %{libname}
Libraries for edje.

%package -n %{devname}
Summary:	Enlightenment edje headers and development libraries
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Requires:	pkgconfig(lua)
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Edje development headers and libraries.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING README
%{_bindir}/%{name}_*
%{_bindir}/inkscape2edc
%{_libdir}/edje/utils/epp
%{_datadir}/%{name}
%{_datadir}/mime/packages/%{name}.xml

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{devname}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}*

