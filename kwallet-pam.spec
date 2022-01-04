#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kwallet-pam
Version  : 5.23.5
Release  : 57
URL      : https://download.kde.org/stable/plasma/5.23.5/kwallet-pam-5.23.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.23.5/kwallet-pam-5.23.5.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1
Requires: kwallet-pam-lib = %{version}-%{release}
Requires: kwallet-pam-license = %{version}-%{release}
Requires: kwallet-pam-services = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules
BuildRequires : kwallet-dev
BuildRequires : libgcrypt-dev

%description
How kwallet-pam works:
During the pam "auth" (pam_authenticate) stage the module gets the password in plain text.
It hashes it against a random salt previously generated by kwallet of random data and keeps it in memory.

%package lib
Summary: lib components for the kwallet-pam package.
Group: Libraries
Requires: kwallet-pam-license = %{version}-%{release}

%description lib
lib components for the kwallet-pam package.


%package license
Summary: license components for the kwallet-pam package.
Group: Default

%description license
license components for the kwallet-pam package.


%package services
Summary: services components for the kwallet-pam package.
Group: Systemd services

%description services
services components for the kwallet-pam package.


%prep
%setup -q -n kwallet-pam-5.23.5
cd %{_builddir}/kwallet-pam-5.23.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641314389
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1641314389
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kwallet-pam
cp %{_builddir}/kwallet-pam-5.23.5/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kwallet-pam/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/kwallet-pam-5.23.5/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kwallet-pam/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/pam_kwallet_init

%files lib
%defattr(-,root,root,-)
/usr/lib64/security/pam_kwallet5.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kwallet-pam/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/kwallet-pam/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/plasma-kwallet-pam.service
