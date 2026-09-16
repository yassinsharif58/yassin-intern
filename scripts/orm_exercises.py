# -*- coding: utf-8 -*-
# Week 2 - Task 06: ORM Methods and Domain Syntax Exercises

def run_exercises(env):
    # 1. All properties with state = 'new'
    # Domain operators used: '=' (equality)
    q1 = env['estate.property'].search([('state', '=', 'new')])

    # 2. Properties where expected_price > 100000
    # Domain operators used: '>' (greater than)
    q2 = env['estate.property'].search([('expected_price', '>', 100000)])

    # 3. Properties in postcode '75001' that have a garden
    # Domain operators used: '=' for string matching, '=' for boolean True
    q3 = env['estate.property'].search([('postcode', '=', '75001'), ('garden', '=', True)])

    # 4. Properties with selling_price between 50000 and 200000
    # Domain operators used: '>=', '<=' (greater/less than or equal)
    q4 = env['estate.property'].search([('selling_price', '>=', 50000), ('selling_price', '<=', 200000)])

    # 5. Properties whose name contains 'villa' (case-insensitive)
    # Domain operators used: 'ilike' (case-insensitive substring containment)
    q5 = env['estate.property'].search([('name', 'ilike', 'villa')])

    # 6. Properties that have at least one offer (offer_ids is not False)
    # Domain operators used: '!=' (not equal to False/empty relation)
    q6 = env['estate.property'].search([('offer_ids', '!=', False)])

    # 7. All properties NOT in state 'sold' or 'cancelled'
    # Domain operators used: 'not in' (exclusion from a tuple/list of values)
    q7 = env['estate.property'].search([('state', 'not in', ('sold', 'cancelled'))])

    # 8. Properties of a specific type (look up type ID first using search())
    # Domain operators used: '=' matching a specific relational record ID
    prop_type = env['estate.property.type'].search([('name', '=', 'Apartment')], limit=1)
    q8 = env['estate.property'].search([('property_type_id', '=', prop_type.id)]) if prop_type else []

    # 9. Properties where date_availability is in the past
    # Domain operators used: '<' (date comparison)
    from datetime import date
    q9 = env['estate.property'].search([('date_availability', '<', date.today())])

    # 10. Properties belonging to the currently logged-in salesperson using env.user
    # Domain operators used: '=' matching the active user's ID
    q10 = env['estate.property'].search([('salesperson_id', '=', env.user.id)])

    return q1, q2, q3, q4, q5, q6, q7, q8, q9, q10