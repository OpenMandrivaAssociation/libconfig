%define major 11
%define libname %mklibname config %{major}
%define libxx %mklibname config++ %{major}
%define devname %mklibname -d config

Summary:	Configuration file parsing library
Name:		libconfig
Version:	1.7.3
Release:	2
Group:		System/Libraries
License:	LGPLv2+
Url:		https://hyperrealm.github.io/libconfig/
Source0:	https://hyperrealm.github.io/libconfig/dist/libconfig-%{version}.tar.gz

%description
libconfig - Consistent configuration library.

Libconfig is a library to provide easy access to configuration
data in a consistent and logical manner. Variables (registered
through lc_register_var(3) or lc_register_callback(3)) are
processed with the lc_process(3) function. Errors can be examined
through lc_geterrno(3) and lc_geterrstr(3).

%package -n %{libname}
Summary:	Configuration file parsing library
Group:		System/Libraries

%description -n %{libname}
libconfig - Consistent configuration library.

Libconfig is a library to provide easy access to configuration
data in a consistent and logical manner. Variables (registered
through lc_register_var(3) or lc_register_callback(3)) are
processed with the lc_process(3) function. Errors can be examined
through lc_geterrno(3) and lc_geterrstr(3).

%package -n %{libxx}
Summary:	Configuration file parsing library
Group:		System/Libraries
Conflicts:	%{libname} < 1.4.8-1

%description -n %{libxx}
libconfig++ - Consistent configuration library.

%package -n %{devname}
Summary:	Development library and header files for the %{name} library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libxx} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}%{name}0-devel < 1.7.3

%description -n	%{devname}
This package contains the development %{name} libraries and its header
files.

%prep
%autosetup -p1

%build
%configure \
	--disable-static

%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libconfig.so.%{major}*

%files -n %{libxx}
%{_libdir}/libconfig++.so.%{major}*

%files -n %{devname}
%doc README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_infodir}/*
%{_libdir}/cmake/libconfig
%{_libdir}/cmake/libconfig++
