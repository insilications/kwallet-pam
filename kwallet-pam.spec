#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : kwallet-pam
Version  : 5.17.3
Release  : 27
URL      : https://download.kde.org/stable/plasma/5.17.3/kwallet-pam-5.17.3.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.17.3/kwallet-pam-5.17.3.tar.xz
Source1 : https://download.kde.org/stable/plasma/5.17.3/kwallet-pam-5.17.3.tar.xz.sig
Summary  : KWallet PAM integration
Group    : Development/Tools
License  : LGPL-2.1
Requires: kwallet-pam-data = %{version}-%{release}
Requires: kwallet-pam-lib = %{version}-%{release}
Requires: kwallet-pam-license = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libgcrypt-dev

%description
How kwallet-pam works:
During the pam "auth" (pam_authenticate) stage the module gets the password in plain text.
It hashes it against a random salt previously generated by kwallet of random data and keeps it in memory.

%package data
Summary: data components for the kwallet-pam package.
Group: Data

%description data
data components for the kwallet-pam package.


%package lib
Summary: lib components for the kwallet-pam package.
Group: Libraries
Requires: kwallet-pam-data = %{version}-%{release}
Requires: kwallet-pam-license = %{version}-%{release}

%description lib
lib components for the kwallet-pam package.


%package license
Summary: license components for the kwallet-pam package.
Group: Default

%description license
license components for the kwallet-pam package.


%prep
%setup -q -n kwallet-pam-5.17.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573577274
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1573577274
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kwallet-pam
cp %{_builddir}/kwallet-pam-5.17.3/COPYING.LIB %{buildroot}/usr/share/package-licenses/kwallet-pam/01a6b4bf79aca9b556822601186afab86e8c4fbf
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/pam_kwallet_init

%files data
%defattr(-,root,root,-)
/usr/share/xdg/autostart/pam_kwallet_init.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/security/pam_kwallet5.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kwallet-pam/01a6b4bf79aca9b556822601186afab86e8c4fbf
