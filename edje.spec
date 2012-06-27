#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/edje edje; \
#cd edje; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
#cd ..; \
#tar -Jcf edje-$PKG_VERSION.tar.xz edje/ --exclude .svn --exclude .*ignore

%define snapshot 0

%if %snapshot
%define	svndate	20120103
%define	svnrev	66793
%endif

%define	major 1
%define	libname %mklibname %{name} %{major}
%define	develname %mklibname %{name} -d

Summary:	Complex graphical design & layout library
Name:		edje
%if %snapshot
Version:	1.1.99.%{svnrev}
Release:	0.%{svndate}.1
%else
Version:	1.2.1
Release:	1
%endif
License:	BSD
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
%if %snapshot
Source0:	%{name}-%{version}.tar.xz
%else
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.gz
%endif

BuildRequires:	lua-devel
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(embryo)
Conflicts:	%{libname} < 1.1.99.66793-0.20120103.1

%description
A graphical layout and animation library for animated resizable, compressed
and scalable themes.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %{libname}
Summary:	Libraries for the edje package
Group:		System/Libraries
Obsoletes:	%{_lib}edje0

%description -n %{libname}
Libraries for edje.

%package -n %{develname}
Summary:	Enlightenment edje headers and development libraries
Group:		Development/Other
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Edje development headers and libraries.

%prep
%if %snapshot
%setup -qn %{name}
%else
%setup -q
%endif

%build
%if %snapshot
NOCONFIGURE=yes ./autogen.sh
%endif

%configure2_5x \
	--disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc AUTHORS COPYING README
%{_bindir}/%{name}_*
%{_bindir}/inkscape2edc
%{_libdir}/edje/utils/epp
%{_libdir}/edje/modules/multisense_factory/*
%{_datadir}/%{name}
%{_datadir}/mime/packages/%{name}.xml

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}*

