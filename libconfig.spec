%define	major 9
%define libname	%mklibname config %{major}
%define libxx	%mklibname config++ %{major}
%define develname	%mklibname -d config

Summary:	Configuration file parsing library
Name:		libconfig
Version:	1.4.8
Release:	1
Group:		System/Libraries
License:	LGPLv2+
URL:		http://www.hyperrealm.com/libconfig/
Source0:	http://www.hyperrealm.com/libconfig/%{name}-%{version}.tar.gz

%description
libconfig - Consistent configuration library.

Libconfig is a library to provide easy access to configuration
data in a consistent and logical manner. Variables (registered
through lc_register_var(3) or lc_register_callback(3)) are
processed with the lc_process(3) function. Errors can be examined
through lc_geterrno(3) and lc_geterrstr(3).

%package -n	%{libname}
Summary:	Configuration file parsing library
Group:		System/Libraries

%description -n	%{libname}
libconfig - Consistent configuration library.

Libconfig is a library to provide easy access to configuration
data in a consistent and logical manner. Variables (registered
through lc_register_var(3) or lc_register_callback(3)) are
processed with the lc_process(3) function. Errors can be examined
through lc_geterrno(3) and lc_geterrstr(3).

%package -n	%{libxx}
Summary:	Configuration file parsing library
Group:		System/Libraries
Conflicts:	%{libname} < 1.4.8-1

%description -n	%{libxx}
libconfig++ - Consistent configuration library.

%package -n	%{develname}
Summary:	Static library and header files for the %{name} library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libxx} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:  %_lib%{name}0-devel

%description -n	%{develname}
This package contains the development %{name} libraries and its header
files.

%prep
%setup -q

%build
%configure2_5x

# fix soname
#perl -pi -e "s|^SHOBJFLAGS.*|SHOBJFLAGS=-Wl,-soname=%{name}.so.%{major} -shared -fPIC -D_REENTRANT|g" Makefile

%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files -n %{libname}
%{_libdir}/libconfig.so.%{major}*

%files -n %{libxx}
%{_libdir}/libconfig++.so.%{major}*

%files -n %{develname}
%doc README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_infodir}/*
%{_bindir}/libconfig_tests

