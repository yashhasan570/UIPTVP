package com.ipvio.stream

import android.content.Context
import androidx.compose.runtime.Composable
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.sp

/** Contact info of the maintainer (Telegram). */
object Contact {
    const val HANDLE = "@johnconstantine570"
    const val URL = "https://t.me/johnconstantine570"
}

/** Settings > Contact: maintainer handle and link (no button: TVs often have no browser). */
@Composable
internal fun ContactSection(@Suppress("UNUSED_PARAMETER") ctx: Context) {
    SectionTitle("Kontakt")
    Hint("Universal IPTV Player is free, ad-free and open source (GPL-3.0). Questions or feedback? Reach the maintainer on Telegram.")
    Text(Contact.HANDLE, color = Accent2, fontSize = 18.sp, fontWeight = FontWeight.Bold, raw = true)
    Text(Contact.URL.removePrefix("https://"), color = Muted, fontSize = 15.sp, raw = true)
}
