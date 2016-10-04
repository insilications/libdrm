#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libdrm
Version  : 2.4.71
Release  : 21
URL      : http://dri.freedesktop.org/libdrm/libdrm-2.4.71.tar.gz
Source0  : http://dri.freedesktop.org/libdrm/libdrm-2.4.71.tar.gz
Summary  : Userspace interface to kernel DRM services
Group    : Development/Tools
License  : MIT
Requires: libdrm-lib
Requires: libdrm-doc
BuildRequires : docbook-xml
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cunit)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(pthread-stubs)
BuildRequires : pkgconfig(valgrind)

%description
libdrm - userspace library for drm
This  is libdrm,  a userspace  library for  accessing the  DRM, direct
rendering  manager, on  Linux,  BSD and  other  operating systes  that
support the  ioctl interface.  The library  provides wrapper functions
for the  ioctls to avoid  exposing the kernel interface  directly, and
for chipsets with drm memory manager, support for tracking relocations
and  buffers.   libdrm  is  a  low-level library,  typically  used  by
graphics drivers  such as the Mesa  DRI drivers, the  X drivers, libva
and  similar projects.  New  functionality in  the kernel  DRM drivers
typically requires  a new  libdrm, but a  new libdrm will  always work
with an older kernel.

%package dev
Summary: dev components for the libdrm package.
Group: Development
Requires: libdrm-lib
Provides: libdrm-devel

%description dev
dev components for the libdrm package.


%package doc
Summary: doc components for the libdrm package.
Group: Documentation

%description doc
doc components for the libdrm package.


%package lib
Summary: lib components for the libdrm package.
Group: Libraries

%description lib
lib components for the libdrm package.


%prep
%setup -q -n libdrm-2.4.71

%build
export LANG=C
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
%configure --disable-static --enable-udev --disable-radeon --disable-nouveau --enable-intel
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/libdrm/amdgpu.h
/usr/include/libdrm/amdgpu_drm.h
/usr/include/libdrm/drm.h
/usr/include/libdrm/drm_fourcc.h
/usr/include/libdrm/drm_mode.h
/usr/include/libdrm/drm_sarea.h
/usr/include/libdrm/i915_drm.h
/usr/include/libdrm/intel_aub.h
/usr/include/libdrm/intel_bufmgr.h
/usr/include/libdrm/intel_debug.h
/usr/include/libdrm/mach64_drm.h
/usr/include/libdrm/mga_drm.h
/usr/include/libdrm/nouveau_drm.h
/usr/include/libdrm/qxl_drm.h
/usr/include/libdrm/r128_drm.h
/usr/include/libdrm/radeon_drm.h
/usr/include/libdrm/savage_drm.h
/usr/include/libdrm/sis_drm.h
/usr/include/libdrm/tegra_drm.h
/usr/include/libdrm/vc4_drm.h
/usr/include/libdrm/via_drm.h
/usr/include/libdrm/virtgpu_drm.h
/usr/include/libdrm/vmwgfx_drm.h
/usr/include/libkms/libkms.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
%doc /usr/share/man/man7/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
