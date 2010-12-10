Summary:	A xosd on screen display plugin for gmpc
Name:		gmpc-osd
Version:	0.18.0
Release:	%mkrel 2
License:	GPLv2+
Group:		Sound
Url:		http://www.sarine.nl//xosd-on-screen-display
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	libmpd-devel >= 0.15.98
BuildRequires:	libxml2-devel
BuildRequires:	gtk+2-devel >= 2.4
BuildRequires:	xosd-devel
BuildRequires:	gmpc-devel >= 0.15.98
Requires:	gmpc
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A xosd on screen display plugin for gmpc.

%prep
%setup -q

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/gmpc/plugins/osdplugin.la
%{_libdir}/gmpc/plugins/osdplugin.so
