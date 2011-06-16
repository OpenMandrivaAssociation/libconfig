%define	major 9
%define libname	%mklibname config %{major}
%define libnamedevel	%mklibname -d config

Summary:	Configuration file parsing library
Name:		libconfig
Version:	1.4.7
Release:	%mkrel 1
Group:		System/Libraries
License:	LGPLv2+
URL:		http://www.hyperrealm.com/libconfig/
Source0:	http://www.hyperrealm.com/libconfig/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q

%build
%configure2_5x

# fix soname
#perl -pi -e "s|^SHOBJFLAGS.*|SHOBJFLAGS=-Wl,-soname=%{name}.so.%{major} -shared -fPIC -D_REENTRANT|g" Makefile

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc README
%{_libdir}/*.so.%{major}*

%files -n %{libnamedevel}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_infodir}/*
%{_bindir}/libconfig_tests

