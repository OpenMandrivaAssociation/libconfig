%define	major 0
%define libname	%mklibname config %{major}
%define libnamedevel	%mklibname -d config

%define _disable_ld_no_undefined 1

Summary:	Configuration file parsing library
Name:		libconfig
Version:	0.2.3
Release:	%mkrel 6
Group:		System/Libraries
License:	GPL
URL:		http://www.rkeene.org/oss/libconfig/
Source0:	http://www.rkeene.org/files/oss/libconfig/devel/%{name}-%{version}.tar.gz
Patch0:     libconfig-0.1.21-DESTDIR.diff
BuildRequires:	libopennet-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
libconfig - Consistent configuration library.

Libconfig is a library to provide easy access to configuration
data in a consistent and logical manner. Variables (registered
through lc_register_var(3) or lc_register_callback(3)) are
processed with the lc_process(3) function. Errors can be examined
through lc_geterrno(3) and lc_geterrstr(3).

%package -n	%{libname}
Summary:	Configuration file parsing library
Group:          System/Libraries

%description -n	%{libname}
libconfig - Consistent configuration library.

Libconfig is a library to provide easy access to configuration
data in a consistent and logical manner. Variables (registered
through lc_register_var(3) or lc_register_callback(3)) are
processed with the lc_process(3) function. Errors can be examined
through lc_geterrno(3) and lc_geterrstr(3).

%package -n	%{libnamedevel}
Summary:	Static library and header files for the %{name} library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}
Obsoletes:  %_lib%{name}0-devel

%description -n	%{libnamedevel}
libconfig - Consistent configuration library.

Libconfig is a library to provide easy access to configuration
data in a consistent and logical manner. Variables (registered
through lc_register_var(3) or lc_register_callback(3)) are
processed with the lc_process(3) function. Errors can be examined
through lc_geterrno(3) and lc_geterrstr(3).

This package contains the static %{name} library and its header
files.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0 -b .destdir

%build
%configure2_5x

# fix soname
perl -pi -e "s|^SHOBJFLAGS.*|SHOBJFLAGS=-Wl,-soname=%{name}.so.%{major} -shared -fPIC -D_REENTRANT|g" Makefile

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc Docs/* README
%{_libdir}/*.so.*

%files -n %{libnamedevel}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_mandir}/man3/*

