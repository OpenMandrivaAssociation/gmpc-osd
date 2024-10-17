Summary:	A xosd on screen display plugin for gmpc
Name:		gmpc-osd
Version:	0.18.0
Release:	3
License:	GPLv2+
Group:		Sound
Url:		https://www.sarine.nl//xosd-on-screen-display
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	libmpd-devel >= 0.15.98
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(gtk+-2.0) >= 2.4
BuildRequires:	xosd-devel
BuildRequires:	gmpc-devel >= 0.15.98
Requires:	gmpc

%description
A xosd on screen display plugin for gmpc.

%prep
%setup -q

%build
%configure2_5x

%make

%install
%makeinstall_std

%files
%{_libdir}/gmpc/plugins/osdplugin.so
