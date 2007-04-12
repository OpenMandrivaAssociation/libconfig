%define	major 0
%define libname	%mklibname config %{major}

Summary:	Libconfig is a configuration file parsing library
Name:		libconfig
Version:	0.1.21
Release:	%mkrel 4
Group:		System/Libraries
License:	GPL
URL:		http://www.rkeene.org/oss/libconfig/
Source0:	http://www.rkeene.org/files/oss/libconfig/devel/%{name}-%{version}.tar.bz2
Patch0:		libconfig-0.1.21-DESTDIR.diff
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
Summary:	Libconfig is a configuration file parsing library
Group:          System/Libraries

%description -n	%{libname}
libconfig - Consistent configuration library.

Libconfig is a library to provide easy access to configuration
data in a consistent and logical manner. Variables (registered
through lc_register_var(3) or lc_register_callback(3)) are
processed with the lc_process(3) function. Errors can be examined
through lc_geterrno(3) and lc_geterrstr(3).

%package -n	%{libname}-devel
Summary:	Static library and header files for the %{name} library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}

%description -n	%{libname}-devel
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
%patch0 -p0

%build

%configure2_5x

# fix soname
perl -pi -e "s|^SHOBJFLAGS.*|SHOBJFLAGS=-Wl,-soname=%{name}.so.%{major} -shared -fPIC -D_REENTRANT|g" Makefile

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc Docs/* README
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_mandir}/man3/*

