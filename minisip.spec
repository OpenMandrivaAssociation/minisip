%define cvs	20061210

Summary: 	Lightweight SIP internet videophone
Name: 	 	minisip
Version: 	0.7.1
Release: 	%mkrel 0.%cvs.2
License:	GPL
Group:		Communications
URL:		http://www.minisip.org/
Source:		%{name}-%{version}-%cvs.tar.bz2
BuildRequires:	pkgconfig ImageMagick
BuildRequires:	libmikey-devel >= 0.4.1-0.20061210.0
BuildRequires:	libmnetutil-devel >= 0.3.1-0.20061210.0
BuildRequires:	libmsip-devel >= 0.3.1-0.20061210.0
BuildRequires:	libmstun-devel >= 0.5.0-0.20061210.0
BuildRequires:	libmutil-devel >= 0.3.1-0.20061210.0
BuildRequires:	libminisip-devel >= 0.3.1-0.20061210.0
BuildRequires:	libglade2.0-devel libglademm-devel openssl-devel >= 0.9.8
BuildRequires:	X11-devel
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Requires:	libminisip-plugins >= 0.3.1-0.20061210.0
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Minisip is a SIP User Agent ("Internet telephone") developed at KTH, Stockholm.

%prep

%setup -q -n %{name}

%build
./bootstrap
%configure2_5x \
    --enable-textui \
    --enable-video

%make
										
%install
rm -rf %{buildroot}

%makeinstall

#menu

#icons
install -d %{buildroot}%{_liconsdir}
install -d %{buildroot}%{_iconsdir}
install -d %{buildroot}%{_miconsdir}

convert -size 48x48 share/tray_icon.png %{buildroot}%{_liconsdir}/%{name}.png
convert -size 32x32 share/tray_icon.png %{buildroot}%{_iconsdir}/%{name}.png
convert -size 16x16 share/tray_icon.png %{buildroot}%{_miconsdir}/%{name}.png

# XDG menu
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=MiniSIP
Comment=SIP Videophone
Exec=%{name}_gtkgui
Icon=%{name}
Terminal=false
Type=Application
Categories=GNOME;GTK;Network;Telephony;X-MandrivaLinux-Internet-VideoConference;
EOF

%find_lang %{name}

%if %mdkversion < 200900
%post
%update_menus
%update_desktop_database
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%clean_desktop_database
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README NEWS TODO
%{_bindir}/*
%{_datadir}/%{name}
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/*.desktop


