Name: x11-driver-video-sisdrv
Version: 0.8.0
Release: %mkrel 1
Summary: The X.org driver provided by SiS for SiS Cards
Group: Development/X11
URL: http://www.sis.com
Source1: sis_drv.so.gz
License: Freeware
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libdrm-devel >= 2.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: GL-devel

Conflicts: xorg-x11-server < 7.0
Conflicts: x11-driver-video-sis

%description
The X.org driver provided by SiS for SiS Cards

%install
mkdir -p %{buildroot}%{_libdir}/xorg/modules/drivers
gunzip -c %{SOURCE1} > %{buildroot}%{_libdir}/xorg/modules/drivers/sis_drv.so

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/sis_drv.so

