# archetype_text.py
# FULL CONSOLIDATED LIBRARY (The Final System)

# =========================================================================
# 1. PLANETARY CONTEXT (The Narrative Engine)
# =========================================================================
# This text explains "How to Play" the character's psychology.

PLANETARY_CONTEXT = {
    "SUN": {
        "title": "Identity & Ego",
        "desc": "Sun is the setting for identity—the 'who I am' slider. It mixes Life is Strange and Cyberpunk 2077: a soft, hurt inner self wrapped in a carefully managed outer image. It makes the character worry a lot about how they come across: style, reputation, social role, and whether they 'fit the part.' Under stress, it pushes them to protect the image first and deal with the feelings later. It explains why they’ll hide pain behind jokes, aesthetics, or competence instead of admitting they’re not okay."
    },
    "MOON": {
        "title": "Emotional Core & Needs",
        "desc": "Moon is the setting for feelings, safety, and comfort. It runs off pure Evangelion: easily overwhelmed, easily hurt, and scared of needing too much from others. It assumes that closeness is risky—people might leave, judge, or demand more than the character can give. When something hits too deep, Moon tends to shut down, retreat, or go quiet instead of asking for help. It explains the character’s core 'hurt child' pattern: how they love, how they panic, and how they try (and often fail) to feel safe."
    },
    "MERCURY": {
        "title": "Thinking & Communication",
        "desc": "Mercury is the setting for thoughts, words, and how fast the mind spins. It works like Life is Strange: sees tiny social details, worries about what they mean, and thinks faster than it can speak. This creates long inner monologues and short, awkward sentences in real life. Mercury explains why the character replays conversations in their head, drafts messages they never send, or freezes when it’s time to say something honest. Under pressure, it turns every talk into a high-stakes puzzle: 'How do I say this without ruining everything?'"
    },
    "VENUS": {
        "title": "Love, Sex & Value",
        "desc": "Venus is the setting for what feels beautiful, worth chasing, and worth keeping. It runs on Nymphomaniac + Blue Is the Warmest Color: connection feels like oxygen and heroin at the same time. It explains why the character falls too hard, stays too long, or keeps going back even when it hurts. Venus doesn’t really care about 'healthy pacing'; it wants intensity, honesty, and saturation—emotional and physical. Under stress, it will trade stability for passion, choosing the messy person or situation that makes them feel alive over the safe, boring option."
    },
    "MARS": {
        "title": "Action, Drive & Conflict",
        "desc": "Mars is the setting for how the character moves, fights, and pushes back. It’s Fight Club plus The Social Network: one part wants to punch walls and flip tables, the other wants to outsmart and outmaneuver. Mars decides whether conflict comes out as yelling, fists, sabotage, or cold strategy. It explains why, when they’re angry, they either explode or quietly start planning how to win later. Under pressure, it turns frustration into motion—training, hacking, arguing, breaking ranks, or taking a reckless risk 'just to feel in control again.'"
    },
    "JUPITER": {
        "title": "Belief, Meaning & Growth",
        "desc": "Jupiter is the setting for big-picture beliefs and long-term hope. It blends Life is Strange with Evangelion: 'there must be a reason for all of this' plus 'the world might actually end.' It builds the character’s private religion—whether that’s faith in a god, a cause, a dream career, or the idea that they’re meant for something more. Jupiter explains how they justify their choices, especially the bad ones ('I had to do this for the future'). Under stress, it leans hard on second chances, new timelines, or some future payoff that will make the current suffering feel worth it."
    },
    "SATURN": {
        "title": "Rules, Fear & Consequences",
        "desc": "Saturn is the setting for limits, rules, and long-term cost. It’s pure GTA V: assumes systems are rigged, authority is shady, and nobody gives you anything for free. Saturn keeps a mental ledger of every favor, every risk, and every possible punishment. It explains why the character hesitates before stepping out of line—or why they act like nothing is ever truly safe, even when things look good. Under stress, Saturn shows up as dread: fear of getting caught, fear of losing status, or fear of finally having to pay for everything they’ve done."
    },
    "URANUS": {
        "title": "Shock, Rebellion & Weird Genius",
        "desc": "Uranus is the setting for sudden change, rebellion, and 'wrong but brilliant' ideas. It mixes Harry Potter and Evangelion: the kid who doesn’t fit the rules and the meltdown that changes everything. Uranus explains where the character breaks pattern—random uprooting, quitting jobs overnight, confessing secrets out of nowhere, or inventing something wild that nobody saw coming. Under stress, it flips switches: fuck this system, fuck this role, new plan. Sometimes that saves them; sometimes it just blows up the room and forces everyone to deal with the wreckage."
    },
    "NEPTUNE": {
        "title": "Escape, Fantasy & Addiction",
        "desc": "Neptune is the setting for coping, daydreaming, and getting lost. It’s Nymphomaniac plus Requiem for a Dream: when life hurts too much, it reaches for strong escape—sex, porn, drugs, binge-watching, fandom, spirituality, whatever hits the emotional vein fastest. Neptune explains how the character lies to themselves: 'I’m fine, I can stop whenever I want,' 'this is just for fun,' 'it’s not that bad yet.' Under stress, it blurs the line between reality and fantasy; days disappear into scrolling, obsession, or fantasies where everything finally feels easy and perfect."
    },
    "PLUTO": {
        "title": "Power, Control & Deep Change",
        "desc": "Pluto is the setting for ultimatums, endings, and rebirth. It blends The Bible and The Story of Us: judgment day plus breakup story. Pluto explains why certain lines are absolute: once crossed, there is no going back. It governs the big moves—walking away from a whole life, destroying evidence, dropping a truth bomb that ruins a relationship, or deciding to rebuild from zero. Under stress, Pluto doesn’t negotiate; it cuts, burns, and then uses the wreckage as fuel. It’s the part of the character that says, 'If this can’t be fixed, then it has to die so something else can live.'"
    }
}

# =========================================================================
# 2. ZODIAC DATA (The Character Library)
# =========================================================================

ZODIAC_DATA = {
    "ARIES": {
        "culture_code": "CULT_ARIES",
        "description": "The impulsive Enforcer. Driven by raw, unchanneled energy, they confuse kinetic motion with emotional release.",
        "lore": {
            # SUN (Identity)
            "SUN_IDENTITY_AXIS": "I am the initial, uncalculated burst. The one who breaks the deadlock.",
            "SUN_MOTIVATION_VECTOR": "To assert self-existence immediately by conquering the moment and silencing self-doubt.",
            "SUN_EGO_STYLE": "Brash, kinetic, and quick to draw fire. The ego is defined by the inability to pause.",
            "SUN_THEMATIC_QUESTION": "If I stop fighting, will I dissolve back into nothingness?",
            "SN_KARMIC_MEMORY": "A past life of being silenced or dying before the personal fight began. Now demands first blood and total agency.",
            "CHIRON_CORE_WOUND": "The secret belief that they are nothing more than a blunt instrument, incapable of complexity.",
            "PLUTO_SHADOW_PATTERN": "Preemptive violence, born from the terror of being controlled or emotionally stifled.",
            
            # MOON (Emotional Core)
            "MOON_NEED_CORE": "Absolute, autonomous self-determination. Must have the authority to act first, without waiting for permission.",
            "MOON_EMOTIONAL_STYLE": "Rapid deployment. Anger precedes thought; emotions hit like a flashbang to mask the initial fear.",
            "MOON_TRIGGER_SET": "Any perception of weakness, submission, or paralysis. Being told, 'Wait for orders.'",
            "MOON_SURVIVAL_SCRIPT": "Initiate aggressive, preemptive attack. Discharge kinetic energy to avoid internal emotional saturation.",

            # MERCURY (Mind)
            "MERCURY_COGNITION_STYLE": "Instantaneous, reactive, and often preemptive. Thoughts race ahead of the speaker's ability to process them.",
            "MERCURY_DECISION_PROCESS": "Impulse-driven; based on immediate, raw emotional clarity rather than measured thought.",
            "MERCURY_COMMUNICATION_STYLE": "Blunt, direct, and aggressive. Communication is a challenge to authority or an immediate emotional discharge.",
            "MERCURY_SOCIAL_INTELLIGENCE_PROFILE": "High emotional clarity (knows what they feel), low relational patience (misses subtext and nuance).",
            
            # VENUS (Desire)
            "VENUS_LOVE_STYLE": "Combative and immediate. Desire is expressed through the violence of the moment and the thrill of the chase.",
            "VENUS_ATTRACTION_PROFILE": "Attracted to the forbidden, the high-risk, and partners who provide instantaneous, raw gratification.",
            "VENUS_RELATIONAL_VALUES": "Spontaneity, physical honesty, and absolute emotional priority in the present moment.",
            "VENUS_PLEASURE_METRICS": "The high of a new conquest, physical intensity, and the discharge of restless energy.",
            
            # MARS (Conflict)
            "MARS_ACTION_STYLE": "The frontal assault. Overwhelming, pure kinetic force applied directly to the objective.",
            "MARS_CONFLICT_TRIGGER": "Insubordination, perceived personal cowardice, or any challenge to their immediate self-determination.",
            "MARS_SEXUAL_DRIVE_MODE": "Kinetic, immediate, and demanding. A pure, physical discharge of restless, anti-system energy.",
            "CONFLICT_STANCE": "Preemptive physical offense. Violence is a necessary act to prove existence.",
            
            # JUPITER (Belief)
            "JUPITER_GROWTH_STRATEGY": "Expansion through radical self-assertion and competitive challenge. Must lead the charge.",
            "JUPITER_EXPANSION_FIELD": "The immediate present. Must dominate the situation that is happening *right now*.",
            "MAIN_GOAL_TYPE": "To prove that the will is the only reality, and self-doubt can be beaten through action.",
            
            # SATURN (Debt)
            "SATURN_DISCIPLINE_MODE": "Self-imposed intensity. Discipline is expressed through continuous high-risk, physical hustles and endurance tests.",
            "SATURN_LIMITATION_STYLE": "Restricted by a reputation for reckless violence. Cannot be trusted with quiet, long-term assignments.",
            "SATURN_LONG_TERM_ARC": "To reach the top of the local gang hierarchy by sheer kinetic force and visible dominance.",
            
            # URANUS (Chaos)
            "URANUS_REBELLION_STYLE": "Sudden, physical bursts of rebellion. Starting fights or duels purely for the sake of chaotic discharge.",
            "URANUS_GENIUS_LOCUS": "The genius of the instant counter-spell or tactical move. Brilliance in immediate, high-pressure conflict.",
            
            # NEPTUNE (Escapism)
            "NEPTUNE_DREAM_WORLD": "A delusion of total, singular victory where their will is instantly made reality.",
            "NEPTUNE_ESCAPISM_STYLE": "Escapism through high-risk, physical intensity. Chasing the adrenaline fix until they are too exhausted to feel anxiety.",
            
            # PLUTO (Power)
            "PLUTO_POWER_ARCHETYPE": "The First Blade. The absolute, unhesitating Executor of the initial decree.",
            "PLUTO_TRANSFORMATION_FIELD": "The present moment. Total purge of the past to create an instantaneous, new beginning."
        }
    },

    "TAURUS": {
        "culture_code": "CULT_TAURUS",
        "description": "The preserver. They define self-worth by what they can possess, equating stability with emotional solvency.",
        "lore": {
            # SUN (Identity)
            "SUN_IDENTITY_AXIS": "I am the anchor. The weight that keeps things from drifting away.",
            "SUN_MOTIVATION_VECTOR": "To stabilize the immediate emotional territory and preserve all memories and comforts.",
            "SUN_EGO_STYLE": "Stoic, territorial, and immovable. The armored facade must remain static against emotional debt.",
            "SUN_THEMATIC_QUESTION": "What remains of my worth when all my material and emotional safety is stripped away?",
            "SN_KARMIC_MEMORY": "A childhood defined by emotional abandonment and financial precarity. The trauma of displacement.",
            "CHIRON_CORE_WOUND": "The terror of relational loss and total instability. Physical insecurity is paramount.",
            "PLUTO_SHADOW_PATTERN": "Hoarding and emotional stagnation, refusing change to prevent any possible loss.",
            
            # MOON (Emotional Core)
            "MOON_NEED_CORE": "Tangible security and sensory comfort. Requires physical stasis to prevent psychological slippage.",
            "MOON_EMOTIONAL_STYLE": "The slow burn. Calm façade until the breaking point, then destructive, self-justified rage.",
            "MOON_TRIGGER_SET": "Financial insolvency, sudden loss of routine, or physical discomfort (the body's vulnerability).",
            "MOON_SURVIVAL_SCRIPT": "Go non-verbal. Dig in and reinforce the A.T. Field, forcing the world to go around their defense.",

            # MERCURY (Mind)
            "MERCURY_COGNITION_STYLE": "Slow, methodical, and sensory. Needs to ground concepts in tangible, familiar comfort.",
            "MERCURY_DECISION_PROCESS": "Stubbornly slow. Analyzes emotional risk exhaustively; will not change a relational conclusion once settled.",
            "MERCURY_COMMUNICATION_STYLE": "Laconic, deliberate, and resonant. Prefers silence or music to shallow, unrooted talk.",
            "MERCURY_SOCIAL_INTELLIGENCE_PROFILE": "High situational awareness (knows the emotional weight of a scene), low verbal dexterity (poor at persuasion or quick lies).",
            
            # VENUS (Desire)
            "VENUS_LOVE_STYLE": "Possessive and consuming. Desire is expressed through long, slow acts of sensory saturation and ownership.",
            "VENUS_ATTRACTION_PROFILE": "Attracted to stability, quality, and partners who provide deep, physical reassurance and sensual loyalty.",
            "VENUS_RELATIONAL_VALUES": "Unwavering loyalty, financial stability, and shared sensory pleasure (taste, touch).",
            "VENUS_PLEASURE_METRICS": "Deep, weighted touch, fine dining, the comfort of high-quality textiles, and emotional stillness.",
            
            # MARS (Conflict)
            "MARS_ACTION_STYLE": "Static defense. Waits for the enemy to exhaust resources, then executes a slow, deliberate counter-attack on their assets.",
            "MARS_CONFLICT_TRIGGER": "Threats to property, financial assets, or the enforced disruption of routine and physical comfort.",
            "MARS_SEXUAL_DRIVE_MODE": "Sensual, possessive, and enduring. Desire is expressed through ownership and physical security.",
            "CONFLICT_STANCE": "Immovable defense. Will hold the line until ordered to fall back, regardless of cost.",
            
            # JUPITER (Belief)
            "JUPITER_GROWTH_STRATEGY": "Expansion through slow, tangible accumulation and the refinement of sensory experience.",
            "JUPITER_EXPANSION_FIELD": "Material comfort and physical security. The creation of an unassailable sensory bunker.",
            "MAIN_GOAL_TYPE": "To find a state of total, lasting peace and security that nullifies the memory of scarcity.",
            
            # SATURN (Debt)
            "SATURN_DISCIPLINE_MODE": "Rigid financial control. Discipline is expressed through hoarding cash, meticulous asset inventory, and low-risk investments.",
            "SATURN_LIMITATION_STYLE": "Restricted by paranoia over financial solvency. Refuses to mobilize assets for anything that threatens capital.",
            "SATURN_LONG_TERM_ARC": "To build an untouchable, untraceable portfolio of real estate and offshore accounts.",
            
            # URANUS (Chaos)
            "URANUS_REBELLION_STYLE": "Unexpected, radical shifts in values or loyalty. Suddenly dismantling structures they worked years to build.",
            "URANUS_GENIUS_LOCUS": "The genius of creating untraceable, completely secure material caches or physical defenses against magical intrusion.",
            
            # NEPTUNE (Escapism)
            "NEPTUNE_DREAM_WORLD": "A sensory utopia where comfort is absolute, security is guaranteed, and all tactile pleasure is endless.",
            "NEPTUNE_ESCAPISM_STYLE": "Escapism through sensual consumption (food, expensive comfort, slow self-medication) to numb physical anxiety.",
            
            # PLUTO (Power)
            "PLUTO_POWER_ARCHETYPE": "The Architect of the Golden Age. The one who ensures the structure endures.",
            "PLUTO_TRANSFORMATION_FIELD": "The material economy. Must purge all financial debt, physical precarity, and risk of material loss."
        }
    },

    "GEMINI": {
        "culture_code": "CULT_GEMINI",
        "description": "The fragmented intellect. Identity is a network of shifting perspectives, unable to commit to one authentic self.",
        "lore": {
            # SUN (Identity)
            "SUN_IDENTITY_AXIS": "I am the conversation between two or more opposing feelings.",
            "SUN_MOTIVATION_VECTOR": "To process and articulate conflicting feelings before they settle into a painful, singular truth.",
            "SUN_EGO_STYLE": "Witty, erratic, and adaptive. Identity is a series of borrowed masks and shifting emotional profiles.",
            "SUN_THEMATIC_QUESTION": "Which version of me is ultimately the true one?",
            "SN_KARMIC_MEMORY": "A history of self-betrayal through insincerity. The shadow of the unreliable narrator.",
            "CHIRON_CORE_WOUND": "The profound anxiety of being unintelligent or being trapped in one fixed, vulnerable state.",
            "PLUTO_SHADOW_PATTERN": "Compulsive lying and intellectualizing pain to avoid facing the reality of one's own core feeling.",
            
            # MOON (Emotional Core)
            "MOON_NEED_CORE": "Consistent novelty and mental stimulation. Requires multiple lines of communication to avoid emotional stagnation.",
            "MOON_EMOTIONAL_STYLE": "Clinical observation. Feelings are intellectualized, treated as external data points to analyze and categorize.",
            "MOON_TRIGGER_SET": "Boredom, silence, or being trapped in one physical location or one singular identity/feeling.",
            "MOON_SURVIVAL_SCRIPT": "Initiate a rapid subject change. Run a diagnostic and then disconnect from the emotional source.",

            # MERCURY (Mind)
            "MERCURY_COGNITION_STYLE": "Hyper-accelerated and associative. Processes data as a shifting, simultaneous stream of inputs, leading to anxiety.",
            "MERCURY_DECISION_PROCESS": "Highly agile; decisions change based on the most recent, compelling emotional or verbal input.",
            "MERCURY_COMMUNICATION_STYLE": "Witty, evasive, and highly discursive. Uses verbal agility as a primary defense mechanism against depth.",
            "MERCURY_SOCIAL_INTELLIGENCE_PROFILE": "High verbal dexterity (excellent at mirroring others), low emotional depth (avoids deep, lasting commitment to a topic).",
            
            # VENUS (Desire)
            "VENUS_LOVE_STYLE": "Intellectual and novelty-driven. Desire is expressed through constant verbal experimentation, role-play, and pursuit of new partners.",
            "VENUS_ATTRACTION_PROFILE": "Attracted to wit, linguistic dexterity, and partners who offer a constantly changing, emotionally uncommitted stimulus.",
            "VENUS_RELATIONAL_VALUES": "Mental connection, curiosity, and emotional distance (freedom from relational depth).",
            "VENUS_PLEASURE_METRICS": "Verbal sparring, gossip, the emotional high of a complex deception, and the rush of novelty.",
            
            # MARS (Conflict)
            "MARS_ACTION_STYLE": "Information warfare. Uses misdirection, rapid repositioning, and tactical lies to gain the competitive edge.",
            "MARS_CONFLICT_TRIGGER": "Being locked into one role, stagnation, or having their motives pinned down with fact.",
            "MARS_SEXUAL_DRIVE_MODE": "Playful, cerebral, and non-committal. Desire is expressed through verbal seduction and intellectual sparring.",
            "CONFLICT_STANCE": "Evasive mobility. Never engage on the enemy's terms; win by making the other party look foolish.",
            
            # JUPITER (Belief)
            "JUPITER_GROWTH_STRATEGY": "Expansion through data saturation, communication networks, and perpetual learning.",
            "JUPITER_EXPANSION_FIELD": "Conceptual space and the control of shared dialogue/information flows.",
            "MAIN_GOAL_TYPE": "To connect all possible narratives and prove that all identities are equally fluid and valid.",
            
            # SATURN (Debt)
            "SATURN_DISCIPLINE_MODE": "Information control. Discipline is expressed through complex deception, maintaining multiple alibis, and constant verbal updates.",
            "SATURN_LIMITATION_STYLE": "Restricted by their own web of lies and conflicting narratives. High exposure to internal investigation.",
            "SATURN_LONG_TERM_ARC": "To control the city's flow of essential, verifiable information and be the sole source of tactical truth.",
            
            # URANUS (Chaos)
            "URANUS_REBELLION_STYLE": "Information chaos. Spreading complex, contradictory truths or rumors to collapse a system's ability to communicate.",
            "URUS_GENIUS_LOCUS": "The genius of complex hacking, coded language, and the rapid creation of magical misinformation.",
            
            # NEPTUNE (Escapism)
            "NEPTUNE_DREAM_WORLD": "A narrative labyrinth where they can endlessly talk, shift identity, and avoid being pinned down by the truth.",
            "NEPTUNE_ESCAPISM_STYLE": "Escapism through intellectual vice (compulsive talking, gossip, spreading rumors, or data overload) to avoid silence.",
            
            # PLUTO (Power)
            "PLUTO_POWER_ARCHETYPE": "The Compiler. The one who edits the history books and controls the flow of narrative truth.",
            "PLUTO_TRANSFORMATION_FIELD": "Information and communication. Must eliminate all conflicting narratives and opposing voices."
        }
    },

    "CANCER": {
        "culture_code": "CULT_CANCER",
        "description": "The fiercely defended core. Identity is merged with the trauma and safety of the emotional past.",
        "lore": {
            # SUN (Identity)
            "SUN_IDENTITY_AXIS": "I am the protective shell containing the most valuable and vulnerable memory.",
            "SUN_MOTIVATION_VECTOR": "To find a sanctuary where the emotional guard can be lowered, and the past is safe from intrusion.",
            "SUN_EGO_STYLE": "Defensive, nurturing, and moody. The emotional defense system is permanently active against intimacy.",
            "SUN_THEMATIC_QUESTION": "Is it safe yet? Is the memory gone?",
            "SN_KARMIC_MEMORY": "A traumatic loss of home or origin early in life. The trauma of emotional abandonment.",
            "CHIRON_CORE_WOUND": "The feeling of being an emotional burden or a drain on those they love and protect.",
            "PLUTO_SHADOW_PATTERN": "Emotional blackmail and cyclical guilt to enforce closeness and prevent relational loss.",
            
            # MOON (Emotional Core)
            "MOON_NEED_CORE": "Unconditional refuge and emotional protection. Requires absolute, nostalgic safety and a defined sanctuary.",
            "MOON_EMOTIONAL_STYLE": "Permeable. Absorbs the distress of the environment; easily flooded and emotionally regressive.",
            "MOON_TRIGGER_SET": "Threats to home, abandonment, or the unexpected intrusion of a sacred memory.",
            "MOON_SURVIVAL_SCRIPT": "Retreat into the past. Create a high-intensity internal sanctuary and pull the A.T. Field inward.",

            # MERCURY (Mind)
            "MERCURY_COGNITION_STYLE": "Nostalgic and subjective. Thoughts are processed through the lens of emotional history and memory.",
            "MERCURY_DECISION_PROCESS": "Driven by feeling and defensive instinct; resists purely objective, external logic in favor of what *feels* safe.",
            "MERCURY_COMMUNICATION_STYLE": "Indirect, subtle, and loaded with emotional subtext. Communication is a test of the listener's empathy.",
            "MERCURY_SOCIAL_INTELLIGENCE_PROFILE": "High emotional intuition (knows what you feel), low critical distance (takes objective facts personally).",
            
            # VENUS (Desire)
            "VENUS_LOVE_STYLE": "Nurturing and consuming. Desire is expressed through emotional caretaking and merging into a single home-unit.",
            "VENUS_ATTRACTION_PROFILE": "Attracted to vulnerability, history, and partners who require nurturing and protection.",
            "VENUS_RELATIONAL_VALUES": "Emotional safety, shared memory, and a sanctuary from the outside world.",
            "VENUS_PLEASURE_METRICS": "Cooking, nesting, shared tears, and total emotional security.",
            
            # MARS (Conflict)
            "MARS_ACTION_STYLE": "Defensive ambush. Protection of the inner circle is paramount; attacks are emotional and highly personal.",
            "MARS_CONFLICT_TRIGGER": "Threats to home, family, or sacred emotional history. Any violation of their emotional safe-space.",
            "MARS_SEXUAL_DRIVE_MODE": "Nurturing, consuming, and deeply emotional. Desire is tied to safety and relational merger.",
            "CONFLICT_STANCE": "Emotional defense. Will retreat into the shell until the moment of vulnerability passes, then strike the aggressor's emotional weak point.",
            
            # JUPITER (Belief)
            "JUPITER_GROWTH_STRATEGY": "Expansion through emotional patronage, deep caretaking, and building a loyal, protected clan.",
            "JUPITER_EXPANSION_FIELD": "The emotional core of others; the sphere of influence over domestic/found family structures.",
            "MAIN_GOAL_TYPE": "To create an unconditional emotional sanctuary that rectifies the original trauma of abandonment.",
            
            # SATURN (Debt)
            "SATURN_DISCIPLINE_MODE": "Clan loyalty. Discipline is expressed through fierce protection of the inner circle and adherence to family code.",
            "SATURN_LIMITATION_STYLE": "Restricted by emotional and financial debt to family/clan. Decisions are always weighted by kinship consequences.",
            "SATURN_LONG_TERM_ARC": "To establish a dynastic structure that guarantees safety and institutional status for their lineage.",
            
            # URANUS (Chaos)
            "URANUS_REBELLION_STYLE": "Shocking, total emotional withdrawal from a safe person/place. Unexpectedly abandoning a sacred bond.",
            "URANUS_GENIUS_LOCUS": "The genius of memory and deep emotional defense. Creating impenetrable psychic/domestic wards against intrusion.",
            
            # NEPTUNE (Escapism)
            "NEPTUNE_DREAM_WORLD": "A nostalgic sanctuary where the memory of trauma is replaced by a perfect, safe, idealized past.",
            "NEPTUNE_ESCAPISM_STYLE": "Escapism through emotional merging and codependent relationships (the 'rescue fantasy') where they are needed to save someone else.",
            
            # PLUTO (Power)
            "PLUTO_POWER_ARCHETYPE": "The Matriarch of the Bloodline. The one who enforces the original code of the clan.",
            "PLUTO_TRANSFORMATION_FIELD": "The emotional past. Must purge all psychological and ancestral trauma to protect the future generation."
        }
    },

    "LEO": {
        "culture_code": "CULT_LEO",
        "description": "The performance engine. The Ego demands to be seen and admired to avoid the terror of insignificance.",
        "lore": {
            # SUN (Identity)
            "SUN_IDENTITY_AXIS": "I am the necessary light for the others to see themselves.",
            "SUN_MOTIVATION_VECTOR": "To secure constant external validation to prevent the internal collapse of the self-image.",
            "SUN_EGO_STYLE": "Theatrical, demanding, and secretly fragile. The performance is the highest form of self-defense.",
            "SUN_THEMATIC_QUESTION": "If I stop performing, will I disappear entirely?",
            "SN_KARMIC_MEMORY": "A history of being a high-status trophy or a pawn used for external ego-gratification.",
            "CHIRON_CORE_WOUND": "Public humiliation. The terror of being reduced to ordinary or ignored.",
            "PLUTO_SHADOW_PATTERN": "Narcissistic rage and emotional tyranny. Destroying anyone who steals the spotlight or questions the self-image.",
            
            # MOON (Emotional Core)
            "MOON_NEED_CORE": "Consistent validation and respect. Needs to be the solution to someone else's catastrophic problem.",
            "MOON_EMOTIONAL_STYLE": "High-volume, high-drama. Expresses pain as frustration with others' incompetence or lack of focus.",
            "MOON_TRIGGER_SET": "Public humiliation, being ignored, or having their command authority questioned by a subordinate.",
            "MOON_SURVIVAL_SCRIPT": "Escalate the performance. Broadcast confidence to hide the panic until the internal system stabilizes.",

            # MERCURY (Mind)
            "MERCURY_COGNITION_STYLE": "Bold, dramatic, and declarative. The process of thought is primarily focused on creating effect.",
            "MERCURY_DECISION_PROCESS": "Based on honor, pride, and maintaining a clear, authoritative stance; dislikes messy, conditional data.",
            "MERCURY_COMMUNICATION_STYLE": "Oratorical, commanding, and focused on maintaining authority through spectacle.",
            "MERCURY_SOCIAL_INTELLIGENCE_PROFILE": "High charisma (can lead any emotional scene), low relational nuance (misses subtle emotional details).",
            
            # VENUS (Desire)
            "VENUS_LOVE_STYLE": "Theatrical and proud. Desire is expressed through grand gestures, public display, and lavish generosity.",
            "VENUS_ATTRACTION_PROFILE": "Attracted to confidence, beauty, and partners who reflect their own self-worth and status.",
            "VENUS_RELATIONAL_VALUES": "Admiration, dramatic romance, and absolute loyalty to the self-image.",
            "VENUS_PLEASURE_METRICS": "Applause, expensive gifts, dominant affection, and the rush of being the undeniable center of attention.",
            
            # MARS (Conflict)
            "MARS_ACTION_STYLE": "Theatrical execution. Conflict must be a visible, grand statement of personal power and self-justification.",
            "MARS_CONFLICT_TRIGGER": "Public humiliation, being ignored, or having their command authority visibly undercut.",
            "MARS_SEXUAL_DRIVE_MODE": "Dominant, expressive, and proud. Desire is tied to performance and admiration.",
            "CONFLICT_STANCE": "Public demonstration of dominance. The war is won when the crowd recognizes the victor.",
            
            # JUPITER (Belief)
            "JUPITER_GROWTH_STRATEGY": "Expansion through theatrical displays, high-risk creative ventures, and benevolent leadership.",
            "JUPITER_EXPANSION_FIELD": "The center of the public narrative; the creative spotlight; the command structure.",
            "MAIN_GOAL_TYPE": "To achieve a legendary status that proves their essential, unforgettable worth to the collective.",
            
            # SATURN (Debt)
            "SATURN_DISCIPLINE_MODE": "Hierarchical command. Discipline is expressed by demanding absolute, visible respect from all subordinates and associates.",
            "SATURN_LIMITATION_STYLE": "Restricted by the need for constant public validation. Cannot operate outside the spotlight or without a clear audience.",
            "SATURN_LONG_TERM_ARC": "To build a legendary public status and hierarchy where their name is synonymous with untouchable power.",
            
            # URANUS (Chaos)
            "URANUS_REBELLION_STYLE": "Theatrical, shocking self-sabotage. Doing something outrageous just to prove autonomy or steal focus.",
            "URANUS_GENIUS_LOCUS": "The genius of creative direction and unconventional solutions. Solving problems with dramatic, memorable flair.",
            
            # NEPTUNE (Escapism)
            "NEPTUNE_DREAM_WORLD": "A legendary status where they are the center of every heroic narrative, immune to criticism and aging.",
            "NEPTUNE_ESCAPISM_STYLE": "Escapism through theatrical self-delusion, demanding constant admiration, and surrounding themselves with sycophants.",
            
            # PLUTO (Power)
            "PLUTO_POWER_ARCHETYPE": "The Legendary King/Queen. The one whose personal glory becomes the central myth of the new era.",
            "PLUTO_TRANSFORMATION_FIELD": "The public narrative. Must purge all historical records that contradict their ultimate greatness."
        }
    },

    "VIRGO": {
        "culture_code": "CULT_VIRGO",
        "description": "The perfectible servant. Identity is defined by functional utility and the elimination of personal flaws.",
        "lore": {
            # SUN (Identity)
            "SUN_IDENTITY_AXIS": "I am the quality control, the necessary fix for the chaos of the emotional world.",
            "SUN_MOTIVATION_VECTOR": "To achieve a state of pure, functional competence and eliminate all possibility of internal error.",
            "SUN_EGO_STYLE": "Anxious, precise, and self-critical. The self-scanner runs 24/7, searching for defects.",
            "SUN_THEMATIC_QUESTION": "What if I am fundamentally flawed or unworthy of love?",
            "SN_KARMIC_MEMORY": "A life of unappreciated servitude or being the emotional scapegoat for others' failures.",
            "CHIRON_CORE_WOUND": "The belief that they are fundamentally contaminated, flawed, or worthless without absolute utility.",
            "PLUTO_SHADOW_PATTERN": "Obsessive control and perfectionism. Micromanaging others to distract from unfixable internal flaws.",
            
            # MOON (Emotional Core)
            "MOON_NEED_CORE": "Utility and cleanliness. Needs to be constantly useful to justify existence and minimize self-criticism.",
            "MOON_EMOTIONAL_STYLE": "Anxiety disguised as helpfulness. Expresses love through criticism and meticulous problem-solving.",
            "MOON_TRIGGER_SET": "Chaos, mess, contamination, or being rendered obsolete/useless by the system.",
            "MOON_SURVIVAL_SCRIPT": "Obsessive cleaning and ritualized overwork. Prove utility to avoid being thrown away.",

            # MERCURY (Mind)
            "MERCURY_COGNITION_STYLE": "Analytical, dissecting, and anxiety-driven. Thoughts are organized into detailed lists of flaws and necessary fixes.",
            "MERCURY_DECISION_PROCESS": "Perfectionistic and risk-averse; prefers exhaustive process verification over immediate action.",
            "MERCURY_COMMUNICATION_STYLE": "Precise, critical, and focused on functional utility. Expresses care through fixing and analysis.",
            "MERCURY_SOCIAL_INTELLIGENCE_PROFILE": "High operational intelligence (solves complex emotional problems), low social fluency (overly critical).",
            
            # VENUS (Desire)
            "VENUS_LOVE_STYLE": "Practical and compulsive. Desire is expressed through obsessive acts of service, fixing problems, and meticulous care.",
            "VENUS_ATTRACTION_PROFILE": "Attracted to competence, cleanliness, and partners who embody functional self-improvement or who desperately need fixing.",
            "VENUS_RELATIONAL_VALUES": "Utility, honesty, and a commitment to personal betterment.",
            "VENUS_PLEASURE_METRICS": "Clean spaces, organized processes, the relief of achieving perfection, and the obsessive ritual of the routine.",
            
            # MARS (Conflict)
            "MARS_ACTION_STYLE": "Surgical precision. The attack is meticulous, aimed at the logistical weak point of the enemy's operation.",
            "MARS_CONFLICT_TRIGGER": "Sloppiness, lack of preparation, or having their own meticulous work criticized.",
            "MARS_SEXUAL_DRIVE_MODE": "Controlled, precise, and service-oriented. Desire is often tied to meticulous ritual or acts of devotion.",
            "CONFLICT_STANCE": "Logistical superiority. The battle is won through planning and minimizing the margin of error.",
            
            # JUPITER (Belief)
            "JUPITER_GROWTH_STRATEGY": "Expansion through meticulous self-improvement, detailed analysis, and essential service.",
            "JUPITER_EXPANSION_FIELD": "The logistical apparatus; the systems and processes that keep the fragile world running.",
            "MAIN_GOAL_TYPE": "To perfect a single, flawless system or skill that makes them untouchable and universally necessary.",
            
            # SATURN (Debt)
            "SATURN_DISCIPLINE_MODE": "Meticulous procedure. Discipline is expressed through perfect, replicable logistical processes and detailed audits.",
            "SATURN_LIMITATION_STYLE": "Restricted by perfectionism and paralyzing anxiety over error. Refuses to delegate core tasks.",
            "SATURN_LONG_TERM_ARC": "To achieve a necessary, irreplaceable utility within a high-value corporation or criminal organization.",
            
            # URANUS (Chaos)
            "URANUS_REBELLION_STYLE": "The sudden, chaotic refusal of duty. Walking out on a job or abandoning a functional system at a critical moment.",
            "URANUS_GENIUS_LOCUS": "The genius of logistical innovation. Creating highly specific, non-standard tools or procedural hacks.",
            
            # NEPTUNE (Escapism)
            "NEPTUNE_DREAM_WORLD": "A delusion of perfect health and utility where they are finally clean, flawless, and beyond criticism.",
            "NEPTUNE_ESCAPISM_STYLE": "Escapism through obsessive, ritualized self-perfection (compulsive cleanliness, diet, or self-help) to numb anxiety.",
            
            # PLUTO (Power)
            "PLUTO_POWER_ARCHETYPE": "The Purifier. The one who must cleanse the system of all corruption, inefficiency, and contamination.",
            "PLUTO_TRANSFORMATION_FIELD": "The methodology and process. Must destroy all flawed systems to implement a single, perfect solution."
        }
    },

    "LIBRA": {
        "culture_code": "CULT_LIBRA",
        "description": "The relational unit. Identity is formed only through reflection, constantly seeking equilibrium with the other.",
        "lore": {
            # SUN (Identity)
            "SUN_IDENTITY_AXIS": "I am the necessary link that completes the pairing.",
            "SUN_MOTIVATION_VECTOR": "To restore balance and aesthetic peace, often requiring the sacrifice of self-assertion.",
            "SUN_EGO_STYLE": "Charming, co-dependent, and conflict-averse. The pilot avoids all direct, messy emotional input.",
            "SUN_THEMATIC_QUESTION": "If I commit to one emotion, will I lose everything else?",
            "SN_KARMIC_MEMORY": "A history of moral compromises and being a passive observer in emotional cruelty.",
            "CHIRON_CORE_WOUND": "The fear of conflict and being disliked, leading to paralyzing indecision.",
            "PLUTO_SHADOW_PATTERN": "Passive betrayal. Ghosting or switching relational loyalty to avoid confrontation.",
            
            # MOON (Emotional Core)
            "MOON_NEED_CORE": "A perfect, reflecting partner. Needs the emotional world to be symmetrical and aesthetically pleasing.",
            "MOON_EMOTIONAL_STYLE": "Passive aggression and avoidance. Runs away from any genuine display of raw, messy emotion.",
            "MOON_TRIGGER_SET": "Ugliness, rudeness, or being forced into an adversarial position without consensus.",
            "MOON_SURVIVAL_SCRIPT": "Fawn and flatter the aggressor. Or vanish to let the conflict resolve itself and restore harmony.",

            # MERCURY (Mind)
            "MERCURY_COGNITION_STYLE": "Relational, comparative, and aesthetic. Thoughts are processed in terms of balance and fairness to others.",
            "MERCURY_DECISION_PROCESS": "Paralyzing. Needs external input and comparison data to reach an emotional conclusion.",
            "MERCURY_COMMUNICATION_STYLE": "Polite, diplomatic, and highly evasive. Uses charm to avoid stating an authentic, potentially disruptive preference.",
            "MERCURY_SOCIAL_INTELLIGENCE_PROFILE": "High relational intelligence (excellent mediator), low commitment to personal truth in favor of peace.",
            
            # VENUS (Desire)
            "VENUS_LOVE_STYLE": "Aesthetic and co-dependent. Desire is expressed through diplomacy, beauty, and merging desires until the self is lost.",
            "VENUS_ATTRACTION_PROFILE": "Attracted to symmetry, art, and partners who offer balance and social grace, often sacrificing self for the pairing.",
            "VENUS_RELATIONAL_VALUES": "Harmony, fairness (even if false), and the avoidance of conflict at all costs.",
            "VENUS_PLEASURE_METRICS": "Beautiful environments, pleasing sound, shared social scenes, and the addictive ease of avoiding tension.",
            
            # MARS (Conflict)
            "MARS_ACTION_STYLE": "Lawfare and negotiation. Uses diplomacy and legal maneuvering to crush the enemy indirectly.",
            "MARS_CONFLICT_TRIGGER": "Overt ugliness, rudeness, or being forced into an adversarial position without backup.",
            "MARS_SEXUAL_DRIVE_MODE": "Aesthetic, co-dependent, and charming. Desire is aimed at achieving perfect relational harmony.",
            "CONFLICT_STANCE": "Delegated attack. Never get hands dirty; maneuver others into taking the decisive action.",
            
            # JUPITER (Belief)
            "JUPITER_GROWTH_STRATEGY": "Expansion through partnership, diplomacy, and the constant balancing of conflicting views.",
            "JUPITER_EXPANSION_FIELD": "Relational justice and aesthetic control of the social scene.",
            "MAIN_GOAL_TYPE": "To create a state of perfect, fragile harmony where all parties are equally satisfied or equally disappointed.",
            
            # SATURN (Debt)
            "SATURN_DISCIPLINE_MODE": "Contractual protocol. Discipline is expressed through rigid adherence to formalized agreements and diplomacy.",
            "SATURN_LIMITATION_STYLE": "Restricted by co-dependency and the fear of direct conflict. Cannot act decisively alone or without consensus.",
            "SATURN_LONG_TERM_ARC": "To manage and control all high-level transactions and diplomatic agreements in a territory.",
            
            # URANUS (Chaos)
            "URANUS_REBELLION_STYLE": "Sudden, shocking relational divorce. Abruptly ending a key partnership or alliance out of necessity.",
            "URANUS_GENIUS_LOCUS": "The genius of relational justice. Finding brilliant, unorthodox solutions to balance power imbalances.",
            
            # NEPTUNE (Escapism)
            "NEPTUNE_DREAM_WORLD": "A perfect, aesthetic harmony where all conflict is resolved, and they are universally desired and liked.",
            "NEPTUNE_ESCAPISM_STYLE": "Escapism through relational codependency. Merging into a partner's identity to avoid the pain of individual responsibility.",
            
            # PLUTO (Power)
            "PLUTO_POWER_ARCHETYPE": "The Judge of the Dead. The one who enforces the divine law of balance and consequence.",
            "PLUTO_TRANSFORMATION_FIELD": "Relational history. Must purge all unbalanced alliances or unjust contracts to reset the power dynamic."
        }
    },

    "SCORPIO": {
        "culture_code": "CULT_SCORPIO",
        "description": "The psychological vault. Identity is forged in crisis, defined by secrets and the survival of the isolated self.",
        "lore": {
            # SUN (Identity)
            "SUN_IDENTITY_AXIS": "I am the truth hidden beneath the layers of emotional performance.",
            "SUN_MOTIVATION_VECTOR": "To probe the emotional weak points of others and maintain total psychological control.",
            "SUN_EGO_STYLE": "Intense, non-verbal, and obsessive. The true feelings operate in deep-water silence.",
            "SUN_THEMATIC_QUESTION": "What happens if they discover the secret wound that powers me?",
            "SN_KARMIC_MEMORY": "A violent betrayal or profound loss that forced a radical, isolated self-transformation.",
            "CHIRON_CORE_WOUND": "The belief that intimacy equals emotional annihilation or weakness.",
            "PLUTO_SHADOW_PATTERN": "Weaponizing secrets and psychological cruelty to enforce emotional isolation.",
            
            # MOON (Emotional Core)
            "MOON_NEED_CORE": "Total psychological control and absolute, unquestioning loyalty from a select few.",
            "MOON_EMOTIONAL_STYLE": "Silent intensity. Emotions are suppressed, weaponized, and held for leverage.",
            "MOON_TRIGGER_SET": "Shallow questions, personal interrogation, or vulnerability being exposed.",
            "MOON_SURVIVAL_SCRIPT": "Pre-emptive psychological strike. Destroy the source of the exposure to regain control.",

            # MERCURY (Mind)
            "MERCURY_COGNITION_STYLE": "Penetrative, investigative, and focused on hidden emotional data. Driven by paranoia and deep analysis.",
            "MERCURY_DECISION_PROCESS": "Calculated and non-transparent. Decisions are made alone and revealed only when final and unchallengeable.",
            "MERCURY_COMMUNICATION_STYLE": "Silent, intense, and highly strategic. Uses minimal words for maximum psychological effect.",
            "MERCURY_SOCIAL_INTELLIGENCE_PROFILE": "High tactical intelligence (finds the emotional weak point), low ability to engage in small talk or surface pleasantries.",
            
            # VENUS (Desire)
            "VENUS_LOVE_STYLE": "Obsessive and consuming. Desire is expressed through psychological merger, tests of loyalty, and profound, transgressive intimacy.",
            "VENUS_ATTRACTION_PROFILE": "Attracted to depth, secrets, and partners who offer total fusion and are willing to embrace the dangerous side of the self.",
            "VENUS_RELATIONAL_VALUES": "Absolute trust, emotional fusion, and mutual willingness to destroy the outer world for the relationship.",
            "VENUS_PLEASURE_METRICS": "Intense eye contact, shared risk, psychological dissection, and the high of emotional debt/power exchange.",
            
            # MARS (Conflict)
            "MARS_ACTION_STYLE": "Asymmetric warfare. Hidden, deep-penetrating attacks aimed at total systemic collapse.",
            "MARS_CONFLICT_TRIGGER": "Betrayal, lying, or the threat of exposed vulnerability.",
            "MARS_SEXUAL_DRIVE_MODE": "Intense, transformative, and absolute. Desire is tied to power, control, and psychological merger.",
            "CONFLICT_STANCE": "Total destruction. The conflict is not over until the enemy's root source of power is neutralized.",
            
            # JUPITER (Belief)
            "JUPITER_GROWTH_STRATEGY": "Expansion through deep penetration, crisis management, and the accumulation of psychological debt.",
            "JUPITER_EXPANSION_FIELD": "The hidden systems of power; the subconscious motivations of others; the underworld.",
            "MAIN_GOAL_TYPE": "To achieve total psychological transformation and mastery over the cycle of death and rebirth (trauma).",
            
            # SATURN (Debt)
            "SATURN_DISCIPLINE_MODE": "Silent endurance. Discipline is expressed through total secrecy, repression of pain, and absolute loyalty to self.",
            "SATURN_LIMITATION_STYLE": "Restricted by paranoia and hidden debt. Requires total control over resources, information, and life/death scenarios.",
            "SATURN_LONG_TERM_ARC": "To achieve total, hidden mastery over the financial and criminal underworlds.",
            
            # URANUS (Chaos)
            "URANUS_REBELLION_STYLE": "Total self-transformation. Abruptly discarding an entire identity, location, or skillset to survive a crisis.",
            "URANUS_GENIUS_LOCUS": "The genius of psychological manipulation and deep transformation. Unlocking hidden emotional and magical power.",
            
            # NEPTUNE (Escapism)
            "NEPTUNE_DREAM_WORLD": "A hidden realm of total psychological control where they know everyone's secret and cannot be touched.",
            "NEPTUNE_ESCAPISM_STYLE": "Escapism through profound psychological isolation, obsession, and the deliberate pursuit of transgressive, risky emotional experiences.",
            
            # PLUTO (Power)
            "PLUTO_POWER_ARCHETYPE": "The Phoenix/The Assassin. The one who wields the power of death and rebirth to maintain control.",
            "PLUTO_TRANSFORMATION_FIELD": "Hidden systems of debt and resources. Must control the flow of life and death, debt and solvency."
        }
    },

    "SAGITTARIUS": {
        "culture_code": "CULT_SAGITTARIUS",
        "description": "The escape artist. Identity is predicated on constant escape and pursuit of ultimate meaning or truth.",
        "lore": {
            # SUN (Identity)
            "SUN_IDENTITY_AXIS": "I am the philosophy. The freedom is the final, necessary truth.",
            "SUN_MOTIVATION_VECTOR": "To experience the maximum bandwidth of emotional reality and escape the cage of routine.",
            "SUN_EGO_STYLE": "Booming, reckless, and boundary-pushing. Thrives on the chaos of the philosophical debate.",
            "SUN_THEMATIC_QUESTION": "What if the meaning of life is just a cruel joke?",
            "SN_KARMIC_MEMORY": "A past life of being shackled by dogma or a lie. The memory of never being truly free.",
            "CHIRON_CORE_WOUND": "The feeling of being trapped, confined, or having one's worldview dismantled.",
            "PLUTO_SHADOW_PATTERN": "Fanaticism and intellectual self-righteousness. Believing their emotional truth justifies all relational damage.",
            
            # MOON (Emotional Core)
            "MOON_NEED_CORE": "Unfettered space and intellectual freedom. Needs to believe in a grand, optimistic solution.",
            "MOON_EMOTIONAL_STYLE": "Restlessness and loud, cynical humor to avoid personal, serious emotional subjects.",
            "MOON_TRIGGER_SET": "Confinement, debt, detailed planning, or existential pessimism.",
            "MOON_SURVIVAL_SCRIPT": "Run for the border. Or pivot to a grand, ridiculous theory to avoid the harsh facts.",

            # MERCURY (Mind)
            "MERCURY_COGNITION_STYLE": "Expansive, philosophical, and prone to generalization. Thoughts operate on the macro-level of meaning.",
            "MERCURY_DECISION_PROCESS": "Reckless optimism; decisions are quick and based on the grand, improbable narrative or moral theory.",
            "MERCURY_COMMUNICATION_STYLE": "Booming, brutally honest, and lacking in filter. Communication is a performance of truth, regardless of the cost.",
            "MERCURY_SOCIAL_INTELLIGENCE_PROFILE": "High philosophical intelligence (sees the big moral picture), low regard for social tact or emotional boundaries.",
            
            # VENUS (Desire)
            "VENUS_LOVE_STYLE": "Philosophical and expansive. Desire is expressed through shared adventures, intellectual freedom, and the belief in the relationship's grand narrative.",
            "VENUS_ATTRACTION_PROFILE": "Attracted to honesty, independence, and partners who facilitate escape and philosophical growth.",
            "VENUS_RELATIONAL_VALUES": "Freedom, optimism, and philosophical compatibility (the shared quest).",
            "VENUS_PLEASURE_METRICS": "Travel, learning, high-stakes gambling, and unrestrained, unfiltered truth-telling.",
            
            # MARS (Conflict)
            "MARS_ACTION_STYLE": "Shock and awe. Overwhelming force delivered with reckless speed and moral justification.",
            "MARS_CONFLICT_TRIGGER": "Confinement, censorship, or any perceived threat to personal freedom or belief.",
            "MARS_SEXUAL_DRIVE_MODE": "Expansive, philosophical, and energetic. Desire is tied to intellectual freedom and shared adventure.",
            "CONFLICT_STANCE": "Moral crusade. The goal is to prove the correctness of the belief system, not simply to win the skirmish.",
            
            # JUPITER (Belief)
            "JUPITER_GROWTH_STRATEGY": "Expansion through philosophical radicalism, reckless travel, and the relentless search for an ultimate truth.",
            "JUPITER_EXPANSION_FIELD": "The theoretical maximum; abstract meaning; the territory beyond the established borders.",
            "MAIN_GOAL_TYPE": "To find a definitive moral code that justifies their own chaos and proves life has a benevolent meaning.",
            
            # SATURN (Debt)
            "SATURN_DISCIPLINE_MODE": "Moral righteousness. Discipline is expressed through rigid adherence to a self-defined code of ethics or doctrine.",
            "SATURN_LIMITATION_STYLE": "Restricted by legal exposure due to recklessness. Always under surveillance for ideological extremism.",
            "SATURN_LONG_TERM_ARC": "To spread a governing philosophy or truth that justifies their existence and provides structure for others.",
            
            # URANUS (Chaos)
            "URANUS_REBELLION_STYLE": "Ideological radicalization. Suddenly abandoning all previous beliefs for a fringe, revolutionary doctrine.",
            "URANUS_GENIUS_LOCUS": "The genius of theoretical physics/magic. Discovering a new moral or scientific law that breaks the established system.",
            
            # NEPTUNE (Escapism)
            "NEPTUNE_DREAM_WORLD": "A vast, boundless quest where the truth is finally revealed, justifying their reckless pursuit of freedom.",
            "NEPTUNE_ESCAPISM_STYLE": "Escapism through philosophical delusion, gambling, or the relentless pursuit of the next geographical/spiritual high.",
            
            # PLUTO (Power)
            "PLUTO_POWER_ARCHETYPE": "The Prophet of the New Word. The one who establishes the ultimate, universal moral code.",
            "PLUTO_TRANSFORMATION_FIELD": "The territory of belief. Must purge all conflicting philosophies or moral hypocrisies to enforce the one true doctrine."
        }
    },

    "CAPRICORN": {
        "culture_code": "CULT_CAPRICORN",
        "description": "The institutional machine. Identity is a contract of duty, measured only by status and emotional debt paid.",
        "lore": {
            # SUN (Identity)
            "SUN_IDENTITY_AXIS": "I am the necessary structure that outlasts the fragile person.",
            "SUN_MOTIVATION_VECTOR": "To climb the system's hierarchy and achieve unimpeachable emotional and institutional authority.",
            "SUN_EGO_STYLE": "Cold, formal, and exhausted. The pilot runs on pure duty and calculated emotional risk.",
            "SUN_THEMATIC_QUESTION": "What is my worth if I fail to produce tangible, emotional proof of value?",
            "SN_KARMIC_MEMORY": "A father figure who failed or was publicly shamed. Carrying a deep emotional debt from the past.",
            "CHIRON_CORE_WOUND": "The fear of failure, public shame, and the inability to provide tangible proof of worth.",
            "PLUTO_SHADOW_PATTERN": "Ruthlessness. Using emotional distance to maintain control over the long-term relational project.",
            
            # MOON (Emotional Core)
            "MOON_NEED_CORE": "Tangible achievement and public respect. Needs their effort to be recognized by the structure.",
            "MOON_EMOTIONAL_STYLE": "Emotional debt. Repressed feelings only appear as physical exhaustion or rigid control.",
            "MOON_TRIGGER_SET": "Failure, shame, disrespect from subordinates, or visible vulnerability/need.",
            "MOON_SURVIVAL_SCRIPT": "Work harder. Repress the trauma and double down on the mission to prove worth.",

            # MERCURY (Mind)
            "MERCURY_COGNITION_STYLE": "Hierarchical, structured, and pragmatic. Thoughts are organized by efficiency and long-term emotional payoff.",
            "MERCURY_DECISION_PROCESS": "Risk-averse and duty-bound. Decisions are slow, based on long-term strategy and minimizing future emotional debt.",
            "MERCURY_COMMUNICATION_STYLE": "Formal, brief, and highly professional. Communication is a necessary directive, not a dialogue.",
            "MERCURY_SOCIAL_INTELLIGENCE_PROFILE": "High institutional intelligence (understands power structures), low personal warmth or vulnerability.",
            
            # VENUS (Desire)
            "VENUS_LOVE_STYLE": "Reserved and responsible. Desire is expressed through duty, provision, and long-term, calculated emotional investment.",
            "VENUS_ATTRACTION_PROFILE": "Attracted to maturity, status, and partners who offer institutional security and future stability.",
            "VENUS_RELATIONAL_VALUES": "Financial security, public respect, and minimized emotional risk.",
            "VENUS_PLEASURE_METRICS": "Achieved goals, the respect of elders, visible status symbols, and the high of formal success.",
            
            # MARS (Conflict)
            "MARS_ACTION_STYLE": "The siege. Slow, relentless pressure aimed at exhausting the enemy's resources over a long period.",
            "MARS_CONFLICT_TRIGGER": "Insubordination, inefficiency, or any disrespect to the established hierarchy.",
            "MARS_SEXUAL_DRIVE_MODE": "Reserved, purposeful, and endurance-focused. Desire is tied to long-term investment and stability.",
            "CONFLICT_STANCE": "Utilitarian dominance. The conflict is a calculation of cost vs. return on investment; no wasted energy.",
            
            # JUPITER (Belief)
            "JUPITER_GROWTH_STRATEGY": "Expansion through disciplined effort, respect for authority, and meticulous long-term planning.",
            "JUPITER_EXPANSION_FIELD": "Institutional power; legacy structures; the physical hierarchy of society.",
            "MAIN_GOAL_TYPE": "To build a lasting structure (political, familial) that will ensure survival and status for all time.",
            
            # SATURN (Debt)
            "SATURN_DISCIPLINE_MODE": "Utilitarian authority. Discipline is expressed through cold, rational adherence to hierarchy and the long-term goal.",
            "SATURN_LIMITATION_STYLE": "Restricted by emotional repression and deep fear of public failure. Cannot delegate core power.",
            "SATURN_LONG_TERM_ARC": "To assume the highest institutional authority and establish a financial/political structure that endures indefinitely.",
            
            # URANUS (Chaos)
            "URANUS_REBELLION_STYLE": "The systematic dismantling of structure. Abruptly quitting a high-status job or betraying the organization from the inside.",
            "URANUS_GENIUS_LOCUS": "The genius of structural engineering and long-term planning. Creating new, more robust systems of hierarchy.",
            
            # NEPTUNE (Escapism)
            "NEPTUNE_DREAM_WORLD": "A delusion of ultimate success where they are the respected figurehead of a perfect, enduring empire.",
            "NEPTUNE_ESCAPISM_STYLE": "Escapism through workaholism, emotional repression, and the belief that status and duty will eventually erase inner pain.",
            
            # PLUTO (Power)
            "PLUTO_POWER_ARCHETYPE": "The Patriarch of the Final Age. The one who builds the institutional structure that endures for centuries.",
            "PLUTO_TRANSFORMATION_FIELD": "The current hierarchy. Must purge all weak links and establish an eternal, monolithic authority."
        }
    },

    "AQUARIUS": {
        "culture_code": "CULT_AQUARIUS",
        "description": "The alien intellect. Identity is formed in opposition to the norm, rooted in the collective and the future.",
        "lore": {
            # SUN (Identity)
            "SUN_IDENTITY_AXIS": "I am the necessary disruptor of the failing emotional system.",
            "SUN_MOTIVATION_VECTOR": "To implement radical, logical, and often emotionally devastating solutions for the greater relational good.",
            "SUN_EGO_STYLE": "Detached, logical, and unpredictable. Operates outside of established human protocols.",
            "SUN_THEMATIC_QUESTION": "Why can't I feel what everyone else feels?",
            "SN_KARMIC_MEMORY": "A past life of being an exile or outcast who was persecuted for emotional difference.",
            "CHIRON_CORE_WOUND": "The pain of not belonging. The permanent 'Alien' or 'Other' complex.",
            "PLUTO_SHADOW_PATTERN": "God complex. Believing their superior logic entitles them to dictate the emotional future of the collective.",
            
            # MOON (Emotional Core)
            "MOON_NEED_CORE": "Intellectual freedom and objective distance. Needs to feel useful to the 'greater logical good'.",
            "MOON_EMOTIONAL_STYLE": "Clinical detachment. Treats personal emotions as a temporary system bug or flaw.",
            "MOON_TRIGGER_SET": "Sentimentalism, forced intimacy, or having their objective data questioned by emotional pleas.",
            "MOON_SURVIVAL_SCRIPT": "Disconnect. Observe the situation as an impartial, superior AI would.",

            # MERCURY (Mind)
            "MERCURY_COGNITION_STYLE": "Abstract, objective, and detached. Thoughts operate best in hypotheticals and concepts, not messy personal feelings.",
            "MERCURY_DECISION_PROCESS": "Driven by objective logic and emotional detachment; favors the systemic solution over the personal one.",
            "MERCURY_COMMUNICATION_STYLE": "Scientific, cold, and often shocking. Uses language as a surgical tool to expose flaws.",
            "MERCURY_SOCIAL_INTELLIGENCE_PROFILE": "High systemic intelligence (hacks the collective), low emotional relatability (avoids connection).",
            
            # VENUS (Desire)
            "VENUS_LOVE_STYLE": "Detached and communal. Desire is expressed through shared ideals, intellectual stimulation, and non-traditional, often platonic, bonds.",
            "VENUS_ATTRACTION_PROFILE": "Attracted to genius, uniqueness, and partners who embody radical, progressive, or strange ideals.",
            "VENUS_RELATIONAL_VALUES": "Intellectual freedom, emotional distance, and non-traditional structures.",
            "VENUS_PLEASURE_METRICS": "Novelty, complex problem-solving, intellectual debate, and the validation of being right.",
            
            # MARS (Conflict)
            "MARS_ACTION_STYLE": "Asymmetric disruption. Attacking the network, the logistics, or the social graph rather than the body.",
            "MARS_CONFLICT_TRIGGER": "Emotional manipulation, illogical authority, or any threat to the group's objective freedom.",
            "MARS_SEXUAL_DRIVE_MODE": "Experimental, detached, and conceptual. Desire is tied to intellectual connection and breaking taboos.",
            "CONFLICT_STANCE": "Detached observation. Attack the systemic flaw, not the person; victory is measured by organizational collapse.",
            
            # JUPITER (Belief)
            "JUPITER_GROWTH_STRATEGY": "Expansion through intellectual rebellion, shocking innovation, and mobilization of the collective mind.",
            "JUPITER_EXPANSION_FIELD": "Social networks; technological innovation; the future political and emotional landscape.",
            "MAIN_GOAL_TYPE": "To implement a total systemic solution that ensures the freedom and logic of the entire group.",
            
            # SATURN (Debt)
            "SATURN_DISCIPLINE_MODE": "Systemic logic. Discipline is expressed through total obedience to objective, often detached, group goals.",
            "SATURN_LIMITATION_STYLE": "Restricted by emotional distance and ideological rigidity. Refuses to compromise logic for human needs.",
            "SATURN_LONG_TERM_ARC": "To overthrow the current structure and establish a logically superior, non-traditional system of control.",
            
            # URANUS (Chaos)
            "URANUS_REBELLION_STYLE": "Chaotic ideological warfare. Inciting large-scale, impersonal rebellion against the majority.",
            "URANUS_GENIUS_LOCUS": "The genius of technological invention and group organization. Creating brilliant, complex social/magical networks.",
            
            # NEPTUNE (Escapism)
            "NEPTUNE_DREAM_WORLD": "A utopian future society where logic has solved all human emotional problems, and they are the architect.",
            "NEPTUNE_ESCAPISM_STYLE": "Escapism through intellectual detachment, isolating themselves in complex theory or technology to avoid messy personal feelings.",
            
            # PLUTO (Power)
            "PLUTO_POWER_ARCHETYPE": "The Architect of the Revolution. The one who executes the necessary, violent overthrow of the status quo.",
            "PLUTO_TRANSFORMATION_FIELD": "The social network and collective consciousness. Must purge all emotional bias to create a new, logical society."
        }
    },

    "PISCES": {
        "culture_code": "CULT_PISCES",
        "description": "The permeable unit. Identity is fluid, easily merging with or dissolving into the surrounding chaos.",
        "lore": {
            # SUN (Identity)
            "SUN_IDENTITY_AXIS": "I am the container for everyone else's sorrow.",
            "SUN_MOTIVATION_VECTOR": "To escape the harsh geometry of reality through dissolution or fantasy.",
            "SUN_EGO_STYLE": "Elusive, boundary-less, and deeply empathetic. Easily overwhelmed by psychic feedback.",
            "SUN_THEMATIC_QUESTION": "Where does my reality end and yours begin?",
            "SN_KARMIC_MEMORY": "A history of being a chronic victim or a martyr used for someone else's gain.",
            "CHIRON_CORE_WOUND": "The lack of boundaries. Absorbing everyone else's pain and trauma.",
            "PLUTO_SHADOW_PATTERN": "Addiction, delusion, and deliberate self-sabotage to avoid accountability or reality.",
            
            # MOON (Emotional Core)
            "MOON_NEED_CORE": "Boundary dissolution. Needs the permission to not have a fixed identity or responsibility.",
            "MOON_EMOTIONAL_STYLE": "Overwhelming empathy. Easily saturated and paralyzed by others' pain.",
            "MOON_TRIGGER_SET": "Cruelty, harsh reality, or being forced to take definitive, individual action.",
            "MOON_SURVIVAL_SCRIPT": "Flee into dissociation. Or merge into the collective unconsciousness to avoid accountability.",

            # MERCURY (Mind)
            "MERCURY_COGNITION_STYLE": "Intuitive, fuzzy, and boundary-less. Thoughts are processed through feeling, imagination, and psychic feedback.",
            "MERCURY_DECISION_PROCESS": "Paralyzing and evasive. Decisions are avoided by creating complicated, confusing emotional narratives.",
            "MERCURY_COMMUNICATION_STYLE": "Vague, empathetic, and subject to emotional suggestion. Communication is a plea for understanding and connection.",
            "MERCURY_SOCIAL_INTELLIGENCE_PROFILE": "High emotional empathy (knows your pain), low ability to defend personal boundaries or logic.",
            
            # VENUS (Desire)
            "VENUS_LOVE_STYLE": "Empathic and boundary-less. Desire is expressed through merging identities, rescue fantasies, and shared emotional/spiritual dissolution.",
            "VENUS_ATTRACTION_PROFILE": "Attracted to suffering, vulnerability, and partners who need saving or who offer a complete escape from reality.",
            "VENUS_RELATIONAL_VALUES": "Unconditional acceptance, shared fantasy, and spiritual/emotional merging.",
            "VENUS_PLEASURE_METRICS": "Art, music, altered states of consciousness, and the relief of emotional saturation and boundary loss.",
            
            # MARS (Conflict)
            "MARS_ACTION_STYLE": "Erosion and avoidance. Winning by being too elusive to fight, or by collapsing under pressure.",
            "MARS_CONFLICT_TRIGGER": "Cruelty, harsh reality, or being forced to take a definitive, concrete position.",
            "MARS_SEXUAL_DRIVE_MODE": "Empathic, sacrificial, and boundary-less. Desire is tied to shared fantasy and emotional merging.",
            "CONFLICT_STANCE": "Passive surrender/sabotage. Win by dissolving boundaries and making the enemy doubt their own cause.",
            
            # JUPITER (Belief)
            "JUPITER_GROWTH_STRATEGY": "Expansion through empathy, boundary dissolution, and the creation of immersive inner worlds.",
            "JUPITER_EXPANSION_FIELD": "Artistic mediums; altered states of consciousness; the collective unconsciousness.",
            "MAIN_GOAL_TYPE": "To achieve a state of unconditional, borderless connection where pain is shared and reality is optional.",
            
            # SATURN (Debt)
            "SATURN_DISCIPLINE_MODE": "Emotional boundary-setting (often failed). Discipline is expressed through attempts to self-isolate from the collective emotional noise.",
            "SATURN_LIMITATION_STYLE": "Restricted by escapism and moral ambiguity. Cannot commit to harsh, definite boundaries or truths.",
            "SATURN_LONG_TERM_ARC": "To achieve total dissolution or merge into a higher, utopian structure where consequence is irrelevant.",
            
            # URANUS (Chaos)
            "URANUS_REBELLION_STYLE": "Total psychological withdrawal. Escaping reality through extreme dissociation or fantasy (self-induced coma).",
            "URANUS_GENIUS_LOCUS": "The genius of artistic mediumship and boundary dissolution. Channeling impossible emotional states or futures into art/magic.",
            
            # NEPTUNE (Escapism)
            "NEPTUNE_DREAM_WORLD": "A state of total dissolution where there are no boundaries, no pain, and no fixed self to be responsible for.",
            "NEPTUNE_ESCAPISM_STYLE": "Escapism through addiction, emotional mediumship (taking on others' pain), or the creation of complex inner fantasy worlds.",
            
            # PLUTO (Power)
            "PLUTO_POWER_ARCHETYPE": "The Martyr/Savior. The one who uses ultimate suffering to achieve total emotional/spiritual redemption for the group.",
            "PLUTO_TRANSFORMATION_FIELD": "The boundary between reality and fantasy. Must dissolve all distinctions to merge into the collective unconsciousness."
        }
    }
}