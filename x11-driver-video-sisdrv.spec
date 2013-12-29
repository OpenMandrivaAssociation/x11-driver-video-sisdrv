Summary:	X.org driver provided by SiS for SiS Cards
Name:		x11-driver-video-sisdrv
Version:	0.8.0
Release:	7
Group:		System/X11
License:	Freeware
Url:		http://www.sis.com
Source1:	sis_drv.so.gz

BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Conflicts:	x11-driver-video-sis

%description
x11-driver-video-sisdrv is the X.org driver provided by SiS for SiS Cards.

%install
mkdir -p %{buildroot}%{_libdir}/xorg/modules/drivers
gunzip -c %{SOURCE1} > %{buildroot}%{_libdir}/xorg/modules/drivers/sis_drv.so

%files
%{_libdir}/xorg/modules/drivers/sis_drv.so

